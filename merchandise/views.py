from django.shortcuts import render
from .models import Team

# Create your views here.

def all_Teams(request):
    """ A view to show all products, including sorting and search queries """

    teams = teams.objects.all()

    context = {
        'teams': teams,
    }

    return render(request, 'merch/.html', context)