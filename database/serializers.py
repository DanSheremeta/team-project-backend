from rest_framework import serializers

from database.models import Description, Pet, Lot


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ("id", "avatar", "name", "surname", "publish_date", "amount", "comment")


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("id",
                  "image",
                  "city",
                  "state",
                  "title",
                  "total_amounts",
                  "current_amounts",
                  "descriptions",
                  "time_created",
                  "colection_author")


class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = ("id",
                  "title",
                  "photos",
                  "description",
                  "start_price",
                  "current_price",
                  "bet_price",
                  "current_winner",
                  "start_date",
                  "end_date",)
