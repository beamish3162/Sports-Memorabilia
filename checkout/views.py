from django.shortcuts import render, reverse, redirect
from django.contrib import message

from .forms import OrderForm
# Create your views here.


def checkout(request):
    cart = request.seesions.get('cart', {})
    if not cart:
        message.erro(request, "cart is empty!")
        return redirect(reverse('home'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context)
