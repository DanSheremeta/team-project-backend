from decimal import Decimal

from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from fundraising.models import Fundraising, Lot
from fundraising.serializers import (
    FundraisingSerializer,
    FundraisingListSerializer,
    FundraisingDetailSerializer,
    FundraisingLotsSerializer,
    LotSerializer,
    LotDetailSerializer,
    BetSerializer,
    BetCreateSerializer,
)


class FundraisingPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class FundraisingViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Fundraising.objects.all()
    # permission_classes = (IsAuthenticated,)
    pagination_class = FundraisingPagination

    def get_serializer_class(self):
        if self.action == "list":
            return FundraisingListSerializer
        if self.action == "retrieve":
            return FundraisingDetailSerializer
        if self.action == "fundraising_lots_list":
            return FundraisingDetailSerializer
        return FundraisingSerializer

    @action(
        methods=["GET"],
        detail=True,
        url_path="lots",
    )
    def fundraising_lots_list(self, request, pk=None) -> Response:
        queryset = self.get_object()
        serializer = FundraisingLotsSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LotViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = Lot.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer) -> None:
        serializer.save(creator=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return LotDetailSerializer
        if self.action == "bet_create":
            return BetCreateSerializer
        return LotSerializer

    @action(
        methods=["POST"],
        detail=True,
        url_path="bet",
    )
    def bet_create(self, request, pk=None) -> Response:
        obj = self.get_object()
        user = request.user
        price = Decimal(request.data["price"])

        if price < (obj.current_price + obj.minimal_step):
            message = {
                "error": "Price should be greater than current price + minimal step!",
            }
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        data = {
            "user": user.id,
            "price": price,
            "lot": obj.id,
        }
        serializer = BetSerializer(data=data)

        if serializer.is_valid():
            bet = serializer.save()

            if obj not in user.tracked_lots.all():
                user.tracked_lots.add(obj)
                user.save()

            obj.current_price = bet.price
            obj.current_bet = bet
            obj.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
