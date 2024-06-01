from rest_framework import serializers

from fundraising.models import Fundraising


class FundraisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraising
        fields = (
            "id",
            "photo",
            "title",
            "description",
            "city",
            "state",
            "money_raised",
            "money_goal",
            "end_at",
        )


class FundraisingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraising
        fields = (
            "id",
            "photo",
            "title",
            "city",
            "state",
            "money_raised",
            "money_goal",
        )


class FundraisingDetailSerializer(serializers.ModelSerializer):
    creator_name = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="creator.name"
    )

    class Meta:
        model = Fundraising
        fields = (
            "id",
            "photo",
            "title",
            "description",
            "city",
            "state",
            "money_raised",
            "money_goal",
            "creator_name",
            "created_at",
            "expires_at",
        )
