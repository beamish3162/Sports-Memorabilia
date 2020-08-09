from django.urls import path
from . import views

urlpatterns = [
    path('<team_id>', views.team_merchandise, name='team_merchandise'),
]
