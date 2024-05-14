from rest_framework import serializers

from app.models import Description, Pet_information


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ("id", "avatar", "name", "surname", "publish_date", "amount", "comment")


class Pet_informationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet_information
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

