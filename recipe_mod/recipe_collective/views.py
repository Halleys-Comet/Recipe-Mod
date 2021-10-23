from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

recipe = [
    {
        'author': 'john', 
        'title': 'beef',
        'content': 'beef',
        'date_posted': 'October 22nd, 2021'
    }
]


def home(request):
    context = {
        'recipe': Recipe.objects.all()
    }

    return render(request, 'recipe_collective/home.html', context)

def about(request):
    return render(request, 'recipe_collective/about.html', {'title': 'About'})

def login(request):
    return render(request, 'recipe_collective/login.html', {'title': 'Login'})