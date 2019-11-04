from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title    = request.POST.get("title")
    title_en = request.POST.get("title_en")
    audience = request.POST.get("audience")
    open_date = request.POST.get("open_date")
    genre = request.POST.get("genre")
    watch_grade = request.POST.get("watch_grade")
    score = request.POST.get("score")
    poster_url = request.POST.get("poster_url")
    description = request.POST.get("description")

    Movie.objects.create(
        title=title,
        title_en=title_en,
        audience=audience,
        open_date=open_date,
        genre=genre,
        watch_grade=watch_grade,
        score=score,
        poster_url=poster_url,
        description=description,
    )
    return redirect("movies:index")

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {'movie': movie}
    return render(request, 'movies/detail.html', context)

def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {'movie': movie}
    return render(request, 'movies/edit.html', context)

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.title = request.POST.get("title") or movie.title
    movie.title_en = request.POST.get("title_en") or movie.title_en
    movie.audience = request.POST.get("audience") or movie.audience
    movie.open_date = request.POST.get("open_date") or movie.open_date
    movie.genre = request.POST.get("genre") or movie.genre
    movie.watch_grade = request.POST.get("watch_grade") or movie.watch_grade
    movie.score = request.POST.get("score") or movie.score
    movie.poster_url = request.POST.get("poster_url") or movie.poster_url
    movie.description = request.POST.get("description") or movie.description
    movie.save()
    return redirect('movies:detail', movie_pk)

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect("movies:index")