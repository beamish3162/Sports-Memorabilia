from django.shortcuts import render,  get_object_or_404
from .models import UserProfile
from checkout.models import Order
from .forms import UserForm
# Create your views here.


def user_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

    form= UserForm(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profiles/user_profile.html', context)


def order_history(request,):
    orders = Order.objects.all()
    profile = get_object_or_404(UserProfile, user=request.user)
    user_orders = profile.orders.all()
    context = {
        'profile':profile,
        'orders': orders,
        'user_orders': user_orders
    }
    return render(request, 'profiles/order_history.html', context)