from django.urls import path 
from . import views
from .data import create_movie_entries
from rest_framework import routers

#function to create initial data, run one time only
#create_movie_entries()

urlpatterns = [
    path('ping', views.ping, name="ping"),
    path('postoffice/<int:PINCODE>', views.getPostOffice, name="getPostOffice"),
    path('active_movies/<int:pincode>', views.onScreenApiView, name="onScreenApiView"),
    path('getMovieRatingByName/<str:movie_title>', views.getMovieRatingByName ,name = "getMovieRatingByName"),
    path('getMovieRatingById/<uuid:movie_id>', views.getMovieRatingById ,name = "getMovieRatingById"),
    #path('give_rating', views.RatingApiView.as_view() ,name = "ratingApiView2"),
    path('give_rating_by_name/<str:movie_title>/<str:username>/<int:rating>', views.give_rating_by_name ,name = "give_rating_by_name"),
    path('give_rating_by_id/<str:movie_id>/<str:user_id>/<int:rating>', views.give_rating_by_id ,name = "give_rating_by_id"),
]

router = routers.DefaultRouter()
router.register("movies", views.MovieViewSet, basename="movieViewSet")
router.register("ratings", views.RatingViewSet, basename = "ratingViewSet")

urlpatterns +=router.urls