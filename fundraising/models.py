import os
import uuid
from django.utils import timezone

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


def fundraising_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/fundraising/", filename)


class Fundraising(models.Model):
    photo = models.ImageField(upload_to=fundraising_image_file_path)
    title = models.CharField(max_length=150)
    description = models.TextField()
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    money_raised = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )
    money_goal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="fundraisings",
    )
    created_at = models.DateTimeField(auto_now=True)
    end_at = models.DateTimeField()

    class Meta:
        ordering = ("created_at", "end_at")
        verbose_name = "fundraising"
        verbose_name_plural = "fundraisings"

    def __str__(self) -> str:
        return f"{self.title} ({self.creator.name})"

    @property
    def expires_at(self):
        now = timezone.now()
        time_delta = self.end_at - now
        days_left = time_delta.days
        hours_left = int(time_delta.seconds / 3600)
        return days_left, hours_left
