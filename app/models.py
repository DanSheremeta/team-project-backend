from django.db import models
from django.db.models import CASCADE


class Description(models.Model):
    avatar = models.ImageField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    amount = models.ImageField()
    comment = models.CharField(max_length=255)


class Pet_information(models.Model):
    image = models.ImageField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    total_amounts = models.IntegerField()
    current_amounts = models.CharField()
    descriptions = models.ForeignKey(Description, on_delete=CASCADE)
    time_created = models.DateTimeField()
    colection_author = models.CharField(max_length=255)
