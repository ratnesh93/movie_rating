from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

from django.db import models


class MovieStatusTypes(models.TextChoices):
    ACTIVE = "active", "Active"
    INACTIVE = "inactive", "Inactive"


class User(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField(blank=True, null=True)


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.TextField(blank=False, null=False)
    year = models.PositiveSmallIntegerField(blank=False, null=False)


class Rating(models.Model):
    # id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
        validators=[MaxValueValidator(10), MinValueValidator(1)],
    )


class Onscreen(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    pincode = models.PositiveSmallIntegerField(null=False, blank=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=32,
        choices=MovieStatusTypes.choices,
        default=MovieStatusTypes.ACTIVE.value,
    )
