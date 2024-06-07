import os
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


class Location(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.state} {self.city}"

    def __repr__(self) -> str:
        return f"{self.state} {self.city}"


def fundraising_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/fundraising/", filename)


class Fundraising(models.Model):
    photo = models.ImageField(upload_to=fundraising_image_file_path)
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="fundraisings",
        null=True,
    )
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
        return f"{self.title} ({self.fundraiser.email})"

    @property
    def count_lots(self) -> int:
        return self.lots.count()


class LotCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class Bet(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="bets",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    lot = models.ForeignKey(
        "Lot",
        on_delete=models.CASCADE,
        related_name="bets",
    )

    def __str__(self) -> str:
        return f"{self.price} - {self.user.email}"


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
        choices=ConditionChoices.choices,
        default=ConditionChoices.NEW,
    )
    category = models.ForeignKey(
        LotCategory,
        on_delete=models.CASCADE,
        related_name="lots",
    )
    current_bet = models.ForeignKey(
        Bet,
        on_delete=models.CASCADE,
        related_name="bet_lots",
        null=True,
        blank=True,
    )
    minimal_step = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    fundraising = models.ForeignKey(
        Fundraising,
        on_delete=models.CASCADE,
        related_name="lots",
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
        return f"{self.title} ({self.creator.email})"
