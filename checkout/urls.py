from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('saved_checkout_info/', views.saved_checkout_info, name='saved_checkout_info'),
    path('wh/', webhook, name='webhook'),
]
