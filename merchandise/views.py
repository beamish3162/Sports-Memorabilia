from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Merchandise


def merchandise_detail(request, merchandise_id):
    """ A view to show individual merchandise pages """

    merchandise = get_object_or_404(Merchandise, pk=merchandise_id)

    context = {
        'merchandise': merchandise,
    }

    return render(request, 'merchandise/merchandise_detail.html', context)


def merchandise_search(request):

    merchandises = Merchandise.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect('home')
            
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        merchandises = merchandises.filter(queries)
    
    context = {
        'merchandises': merchandises,
        'search_term': query,
    }

    return render(request, 'merchandise/merchandise_search.html', context)
