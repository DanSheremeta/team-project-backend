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
            "lot",
        )


class BetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = (
            "id",
            "price",
        )


class BetLotDetailSerializer(serializers.ModelSerializer):
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
            "current_price",
            "fundraising",
            "end_at",
        )

    def validate(self, data):
        fundraising = data.get("fundraising")
        end_at = data.get("end_at")

        if fundraising and end_at and end_at > fundraising.end_at:
            raise serializers.ValidationError(
                {
                    "end_at": f"The lot end date must be less than or equal to "
                              f"the fundraising end date ({fundraising.end_at}).",
                }
            )

        return data


class LotDetailSerializer(serializers.ModelSerializer):
    total_bets = serializers.IntegerField(read_only=True)
    total_participants = serializers.IntegerField(read_only=True)
    current_bet = BetLotDetailSerializer(many=False, read_only=True)
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
            "total_bets",
            "total_participants",
            "created_at",
            "end_at",
        )
