from django.db import models
from django.db.models import CASCADE

from user.models import User


class Description(models.Model):
    avatar = models.ImageField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    amount = models.ImageField()
    comment = models.CharField(max_length=255)


class Pet(models.Model):
    image = models.ImageField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    total_amounts = models.IntegerField()
    current_amounts = models.CharField(max_length=255)
    descriptions = models.ForeignKey(Description, on_delete=CASCADE)
    time_created = models.DateTimeField()
    colection_author = models.CharField(max_length=255)


class Lot(models.Model):
    title = models.CharField(max_length=255)
    photos = ""
    description = models.TextField()
    start_price = models.FloatField()
    current_price = models.FloatField()
    bet_price = models.FloatField()
    current_winner = User
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
