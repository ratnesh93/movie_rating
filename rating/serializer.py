from .models import Movie, Onscreen, Rating, User
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class OnScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onscreen
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    movie_name = serializers.CharField(source="movie.name")

    class Meta:
        model = Rating
        fields = ("id", "user", "movie_name", "rating")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
