from django.shortcuts import render, get_object_or_404
from .models import Team, Merchandise


def team_merchandise(request, team_id):
    """ A view to show individual team pages """

    merchandises = Merchandise.objects.all()
    team = get_object_or_404(Team, pk=team_id)

    context = {
        'team': team,
        'merchandises': merchandises
    }

    return render(request, 'merchandise/team_merchandise.html', context)
