from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
import requests
from .serializer import MovieSerializer, OnScreenSerializer, RatingSerializer,UserSerializer
from .models import Movie, Onscreen, Rating, User,MovieStatusTypes
from rest_framework import filters

def ping(request):
    return HttpResponse("pong")

class MovieViewSet(viewsets.ModelViewSet):
    """
    Urls for movies: 
    1. http://127.0.0.1:8000/rating/movies :  list of all the movies
    2. http://127.0.0.1:8000/rating/movies/id : a movie with primary key
    3. http://127.0.0.1:8000/rating/movies?search=name : a movie search with name
    """
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    queryset = Movie.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    """
    add, delete, update user
    """
    serializer_class= UserSerializer

    
class RatingViewSet(viewsets.ModelViewSet):
    """
    To get rating for a movies
    ---
    """
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()


# Requirement 1: API to submit ratings (between 1-10) by users for a selected movie.
@api_view(['POST'])
def give_rating_by_id(request, movie_id, user_id, rating ):
    """
    Urls to submit rating of a movie
    http://127.0.0.1:8000/rating/give_rating_by_id/{movie_id}/{user_id}/{rating}
    """
    return save_rating(rating,user_id==user_id,movie_id=movie_id)

# Requirement 1: API to submit ratings (between 1-10) by users for a selected movie.
@api_view(['POST'])
def give_rating_by_name(request, movie_title, username, rating ):
    """
    Urls to submit rating of a movies
    http://127.0.0.1:8000/rating/give_rating_by_name/{movie_title}/{username}/{rating}
    """
    return save_rating(rating,username=username,movie_title=movie_title)

def save_rating(rating, username=None,movie_title=None,user_id=None,movie_id=None):
    try:
        movie_obj = None
        if movie_id:
            movie_obj = Movie.objects.filter(id=movie_id).first()
        elif movie_title:
            movie_obj = Movie.objects.filter(name__icontains=movie_title).first()
        else:
            return Response({"message":"please send either movie_id or movie_title"}, status=status.HTTP_400_BAD_REQUEST)
        
        user_obj = None
        if user_id:
            user_obj = User.objects.get(id=user_id)
        elif username:
            user_obj, created = User.objects.get_or_create(name = username)
        else:
            return Response({"message":"please send user details"}, status=status.HTTP_400_BAD_REQUEST)
        if rating:
            rating_obj = Rating.objects.create(
                movie = movie_obj,
                rating = rating,
                user = user_obj
            )
            json_to_send = RatingSerializer(rating_obj).data
            return Response({"data": json_to_send})
        else:
            return Response({"message":"please send rating for the movie"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"message":f"Failed to save ratings due to {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# Requirement 2: API to get the rating (between 1-10) of a selected movie
@api_view()
def getMovieRatingByName(request, movie_title):
    """
    Url to get rating of selected movie:
    http://127.0.0.1:8000/rating/getMovieRatingByName/{movie_title}
    """
    try:
        movie = Movie.objects.filter(name__icontains=movie_title)
        rating = Rating.objects.filter(movie__in=movie)
        json_to_send= RatingSerializer(rating,  many=True).data
        return Response({"count":len(json_to_send),"data":json_to_send})
    except Exception as e:
        print(e)
        return Response({"message": "unable to fetch movie rating"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Requirement 2: API to get the rating (between 1-10) of a selected movie
@api_view()
def getMovieRatingById(request, movie_id):
    """
    Url to get rating of selected movie:
    http://127.0.0.1:8000/rating/getMovieRatingById/{movie_id}
    """
    try:
        movie = Movie.objects.filter(id=movie_id)
        rating = Rating.objects.filter(movie__in=movie)
        json_to_send= RatingSerializer(rating,  many=True).data
        return Response({"count":len(json_to_send),"data":json_to_send})
    except Exception as e:
        print(e)
        return Response({"message": "unable to fetch movie rating"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Requirement 3: API integration for fetching pincodes.
@api_view()
def getPostOffice(request, PINCODE):
    """
    Url to fetch PostOffice details
    1. http://127.0.0.1:8000/rating/postoffice/PINCODE: returns list of postoffices associated with pincode
    """
    url = f'https://api.postalpincode.in/pincode/{PINCODE}'
    response = requests.get(url)
    return Response(response.json())

#Requirement 4: API to search for list of active movies in a pincode.
@api_view()
def onScreenApiView(request, pincode):
    """
    Url to fetch Active movies in a pincode
    1. http://127.0.0.1:8000/rating/active_movies/110001 : get active movies with a particular pincode
    """
    active_movies = Onscreen.objects.filter(pincode = pincode, status= MovieStatusTypes.ACTIVE.value)
    json_to_send = OnScreenSerializer(active_movies, many=True).data
    return Response({"count":len(json_to_send),"data":json_to_send})