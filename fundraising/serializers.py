from rest_framework import serializers

from fundraising.models import Fundraising, Lot, LotCategory


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
    fundraiser_name = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="fundraiser.name"
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
            "fundraiser_name",
            "created_at",
            "expires_at",
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
            "minimal_bet",
            "fundraising",
            "current_winner",
            "end_at",
        )


class LotDetailSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(
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
            "current_bet",
            "creator",
            "created_at",
            "expires_at",
        )
