from django.shortcuts import render
from merchandise.models import Team, League

# Create your views here.


def index(request):

    teams = Team.objects.all()
    Leagues = League.objects.all()

    context = {
        'teams': teams,
        'Leagues': Leagues,
    }
    return render(request, 'home/index.html', context)
