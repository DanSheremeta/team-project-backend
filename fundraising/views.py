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
        return LotSerializer
