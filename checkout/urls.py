from django.urls import path
from . import views
from .webhook import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('saving_checkout_info/', views.saving_checkout_info, name='saving_checkout_info'),
    path('wh/', webhook, name='webhook'),
]
