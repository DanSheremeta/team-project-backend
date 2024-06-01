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
    fundraiser = models.ForeignKey(
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
        return f"{self.title} ({self.fundraiser.name})"

    @property
    def expires_at(self):
        now = timezone.now()
        time_delta = self.end_at - now
        days_left = time_delta.days
        hours_left = int(time_delta.seconds / 3600)
        return days_left, hours_left


class LotCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


def lot_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/lots/", filename)


class Lot(models.Model):
    class ConditionChoices(models.TextChoices):
        NEW = "new", "New"
        USED = "used", "Used"

    photo = models.ImageField(upload_to=lot_image_file_path)
    title = models.CharField(max_length=150)
    description = models.TextField()
    condition = models.CharField(
        max_length=4,
        choices=ConditionChoices,
        default=ConditionChoices.NEW,
    )
    category = models.ForeignKey(
        LotCategory,
        on_delete=models.CASCADE,
        related_name="lots",
    )
    current_bet = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )
    minimal_bet = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    fundraising = models.ForeignKey(
        Fundraising,
        on_delete=models.CASCADE,
        related_name="lots",
    )
    current_winner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="winner_lots",
        null=True,
        blank=True,
    )
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="creator_lots",
    )
    created_at = models.DateTimeField(auto_now=True)
    end_at = models.DateTimeField()

    class Meta:
        ordering = ("created_at", "end_at")
        verbose_name = "lot"
        verbose_name_plural = "lots"

    def __str__(self) -> str:
        return f"{self.title} ({self.creator.name})"

    @property
    def expires_at(self):
        now = timezone.now()
        time_delta = self.end_at - now
        days_left = time_delta.days
        hours_left = int(time_delta.seconds / 3600)
        return days_left, hours_left
