from rest_framework import serializers

from pet.models import Description, Pet


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = (
            "id",
            "avatar",
            "name",
            "surname",
            "publish_date",
            "amount",
            "comment"
        )


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = (
            "id",
            "title",
            "image",
            "city",
            "state",
            "total_amounts",
            "current_amounts",
            "description",
            "collection_author",
        )
