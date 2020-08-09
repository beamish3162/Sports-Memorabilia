from django.urls import path
from . import views

urlpatterns = [
    path('league', views.all_leagues, name='leagues')
]
