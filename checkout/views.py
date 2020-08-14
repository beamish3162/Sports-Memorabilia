from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.contexts import cart_content
from merchandise.models import Merchandise
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    if request.method == 'POST':
        cart = request.session.get('cart', {})
       
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    merchandise = Merchandise.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            merchandise=merchandise,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Merchandise.DoesNotExist:
                    messages.error(request, (
                        "We couldn't find one of the items in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'Hmm somethings not right. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.erro(request, "cart is empty!")
            return redirect(reverse('home'))

        current_cart = cart_content(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,

    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)
