from django.shortcuts import render
from .models import Team, League


def all_leagues(request):
    """ A view to show all products, including sorting and search queries """

    teams = Team.objects.all()
    Leagues = League.objects.all()

    context = {
        'teams': teams,
        'Leagues': Leagues
    }

    return render(request, 'merchandise/league.html', context)

