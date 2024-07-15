from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from user.serializers import UserSerializer
from fundraising.serializers import LotListSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserTrackedLotsListView(generics.ListAPIView):
    serializer_class = LotListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return user.tracked_lots.all()
