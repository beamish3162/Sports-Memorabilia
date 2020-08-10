from django.shortcuts import render, get_object_or_404
from merchandise.models import Team, League, Merchandise

# Create your views here.


def index(request):

    teams = Team.objects.all()
    Leagues = League.objects.all()

    context = {
        'teams': teams,
        'Leagues': Leagues,
    }
    return render(request, 'home/index.html', context)


def team_merchandise(request, team_id):
    """ A view to show individual team pages """

    merchandises = Merchandise.objects.all()
    team = get_object_or_404(Team, pk=team_id)
    # signed = None

    # if request.GET:
    #     if 'signed' in request.GET:
    #         signed = Merchandise.objects.filter(signed=True)
    context = {
        'team': team,
        'merchandises': merchandises,
        # 'is_signed': signed
    }

    return render(request, 'home/team_merchandise.html', context)

