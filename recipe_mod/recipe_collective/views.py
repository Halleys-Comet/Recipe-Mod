from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'John', 
        'title': 'post',
        'content': 'first', 
        'date_posted': 'today'
    },
    {
        'author': 'john1',
        'title': 'post1',
        'content': 'first1', 
        'date_posted': 'today1'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'recipe_collective/home.html', context)

def about(request):
    return render(request, 'recipe_collective/about.html', {'title': 'About'})