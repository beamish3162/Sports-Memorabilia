from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:team_id>', views.team_merchandise, name='team_merchandise'),
]
