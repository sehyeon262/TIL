from django.shortcuts import render
from django.views.decorators.http import require_safe
from django.http import JsonResponse
from .models import Movie, Genre


@require_safe
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/index.html', context)


def filter_genre(request):
    genre_pk = request.GET.get('genre_pk')

    if genre_pk:
        movies = Movie.objects.filter(genres__pk=genre_pk)
    else:
        movies = Movie.objects.all()

    movies_data = []
    for movie in movies:
        movies_data.append({
            'id': movie.pk,
            'title': movie.title,
            'release_date': movie.release_date,
            'popularity': movie.popularity,
            'vote_count': movie.vote_count,
            'vote_average': movie.vote_average,
            'overview': movie.overview,
            'poster_path': movie.poster_path,
        })

    return JsonResponse({'movies': movies_data})


@require_safe
def recommended(request):
    pass
