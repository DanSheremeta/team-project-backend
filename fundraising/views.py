from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from fundraising.models import Fundraising
from fundraising.serializers import (
    FundraisingSerializer,
    FundraisingListSerializer,
    FundraisingDetailSerializer,
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
        return FundraisingSerializer
