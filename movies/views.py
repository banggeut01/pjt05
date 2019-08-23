from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-id') # 최신글순
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.GET.get('title')
    title_en = request.GET.get('title_en')
    audience = request.GET.get('audience')
    open_date = request.GET.get('open_date')
    genre = request.GET.get('genre')
    watch_grade = request.GET.get('watch_grade')
    score = request.GET.get('score')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')
    movie = Movie.objects.create(title=title, title_en=title_en, audience=audience, \
         open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, \
             poster_url=poster_url, description=description)
    return redirect(f'/movies/{movie.pk}/')

def detail(request, movie_pk):
    movie = Movie.objects.get(id=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

def edit(request, movie_pk):
    movie = Movie.objects.get(id=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/edit.html', context)
    
def update(request, movie_pk):
    title = request.GET.get('title')
    title_en = request.GET.get('title_en')
    audience = request.GET.get('audience')
    open_date = request.GET.get('open_date')
    genre = request.GET.get('genre')
    watch_grade = request.GET.get('watch_grade')
    score = request.GET.get('score')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')
    movie = Movie.objects.get(pk=movie_pk)
    movie.title=title 
    movie.title_en=title_en
    movie.audience=audience
    movie.open_date=open_date
    movie.genre=genre
    movie.watch_grade=watch_grade
    movie.score=score
    movie.poster_url=poster_url
    movie.description=description
    movie.save()
    return redirect(f'/movies/{movie.pk}/')


def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('/movies/')
