import uuid

from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField(blank=True,null=True)


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    name = models.TextField(blank=False, null=False)
    year = models.PositiveSmallIntegerField(blank=False, null=False)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(blank=False, null=False)

class Onscreen(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    pincode = models.PositiveSmallIntegerField(null=False, blank=False)
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE)

