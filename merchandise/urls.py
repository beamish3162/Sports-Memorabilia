from django.urls import path
from . import views

urlpatterns = [
    path('<merchandise_id>', views.merchandise_detail,
         name='merchandise_detail'),
    path('', views.merchandise_search, name='merchandise_search'),
]
