from django.shortcuts import render, get_object_or_404
from merchandise.models import Team, League, Merchandise

# Create your views here.


def index(request):

    Leagues = League.objects.all()
    teams = Team.objects.order_by('name')

    context = {
        'teams': teams,
        'Leagues': Leagues,
    }
    return render(request, 'home/index.html', context)


def team_merchandise(request, team_id):
    """ A view to show individual team pages """

    merchandises = Merchandise.objects.all()
    team = get_object_or_404(Team, pk=team_id)
    merch = Merchandise.objects.filter(team=team)
    sort = None
    direction = None

    if request.GET:
        if 'signed' in request.GET:
            merchandises = Merchandise.objects.filter(signed=True)
        if 'game_used' in request.GET:
            merchandises = Merchandise.objects.filter(game_used=True)
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            merchandises = merchandises.order_by(sortkey)
    current_sorting = f'{sort}_{direction}'
    context = {
        'team': team,
        'merchandises': merchandises,
        'current_sorting': current_sorting,
        'merch': merch
    }

    return render(request, 'home/team_merchandise.html', context)
