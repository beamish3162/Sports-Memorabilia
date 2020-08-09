from django.shortcuts import render, get_object_or_404
from .models import Merchandise


def merchandise_detail(request, merchandise_id):
    """ A view to show individual merchandise pages """

    merchandise = get_object_or_404(Merchandise, pk=merchandise_id)

    context = {
        'merchandise': merchandise,
    }

    return render(request, 'merchandise/merchandise_detail.html', context)
