from rest_framework import serializers

from fundraising.models import Fundraising, Lot, Location, Bet
from user.serializers import UserFullNameSerializer


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            "id",
            "city",
            "state",
        )


class FundraisingSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = Fundraising
        fields = (
            "id",
            "photo",
            "title",
            "description",
            "location",
            "money_raised",
            "money_goal",
            "end_at",
        )


class FundraisingListSerializer(serializers.ModelSerializer):
    count_lots = serializers.IntegerField(read_only=True)
    location = LocationSerializer(many=False, read_only=True)

    class Meta:
        model = Fundraising
        fields = (
            "id",
            "photo",
            "title",
            "location",
            "money_raised",
            "money_goal",
            "count_lots",
        )


class FundraisingDetailSerializer(serializers.ModelSerializer):
    fundraiser = UserFullNameSerializer(many=False, read_only=True)
    location = LocationSerializer(many=False, read_only=True)

    class Meta:
        model = Fundraising
        fields = (
            "id",
            "photo",
            "title",
            "description",
            "location",
            "money_raised",
            "money_goal",
            "fundraiser",
            "created_at",
            "end_at",
        )


class LotListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )

    class Meta:
        model = Lot
        fields = (
            "id",
            "photo",
            "title",
            "description",
            "condition",
            "category",
            "current_bet",
        )


class FundraisingLotsSerializer(serializers.ModelSerializer):
    lots = LotListSerializer(many=True, read_only=True)

    class Meta:
        model = Fundraising
        fields = (
            "id",
            "title",
            "lots",
        )


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = (
            "id",
            "user",
            "price",
        )


class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = (
            "id",
            "photo",
            "title",
            "description",
            "condition",
            "category",
            "minimal_step",
            "fundraising",
            "end_at",
        )


class LotDetailSerializer(serializers.ModelSerializer):
    current_bet = BetSerializer(many=False, read_only=True)
    creator = UserFullNameSerializer(many=False, read_only=True)

    class Meta:
        model = Lot
        fields = (
            "id",
            "photo",
            "title",
            "description",
            "current_bet",
            "minimal_step",
            "creator",
            "created_at",
            "end_at",
        )
