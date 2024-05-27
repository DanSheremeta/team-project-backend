import os
import uuid

from django.db import models
from django.db.models import CASCADE
from django.utils.text import slugify


def description_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.name)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/description/", filename)

class Description(models.Model):
    avatar = models.ImageField(upload_to=description_image_file_path)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    publish_date = models.DateField()
    amount = models.IntegerField()
    comment = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"


def pet_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/pets/", filename)


class Pet(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=pet_image_file_path)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    total_amounts = models.IntegerField()
    current_amounts = models.IntegerField()
    description = models.ForeignKey(
        Description,
        on_delete=CASCADE,
        related_name="pets"
    )
    collection_author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
