from django.shortcuts import render


def index(request, slug_name=None):
    context = {}
    return render(request, 'menu/main.html', context)
