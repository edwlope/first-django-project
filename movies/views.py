
from django.shortcuts import render, HttpResponse


def index(request):
    context = {
        'movies': [
            'gladiator',
            'top gun',
            'casino',
            'spirited away',
            'dragonball z',
            'jujutsu kaisen']
    }
    return render(request, 'movies/index.html', context)


def about(request):
    return render(request, 'movies/about.html', {})
