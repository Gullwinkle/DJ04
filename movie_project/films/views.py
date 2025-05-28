from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def index(request):
    films = Movie.objects.all()
    return render(request, 'films/index.html', {
        'films': films,
        'active_page': 'main',
    })

def add_movie(request):
    error = ''
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Ошибка при заполнении формы'
    form = MovieForm()
    return render(request, 'films/add_movie.html', {
        'active_page': 'add_movie',
        'form': form,
        'error': error
    })
