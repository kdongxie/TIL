from django.shortcuts import render, redirect
from .models import Movie
from django.db import IntegrityError
# Create your views here.
def index(request):
    movies = Movie.objects.all()[::-1]
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        title_origin = request.POST.get('title_origin')
        vote_count = request.POST.get('vote_count')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        movie = Movie(title=title,
                      title_origin=title_origin,
                      vote_count=vote_count,
                      open_date=open_date,
                      genre=genre,
                      score=score,
                      poster_url=poster_url,
                      description=description,)
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        return render(request, 'movies/create.html')

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {'movie': movie}
    return render(request, 'movies/detail.html', context)

def delete(request, movie_pk):
    if request.method =='POST':
        movie = Movie.objects.get(pk=movie_pk)
        movie.delete()
        return redirect('movies:index')
    else:
        return render(request, 'movies/detail.html')

def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.title_origin = request.POST.get('title_origin')
        movie.vote_count = request.POST.get('vote_count')
        movie.open_date = request.POST.get('open_date')
        movie.genre = request.POST.get('genre')
        movie.score = request.POST.get('score')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        context = {'movie': movie}
        return render(request, 'movies/edit.html', context)
