from rest_framework import viewsets
from pet.serializers import PetSerializer, DescriptionSerializer

from pet.models import Pet, Description


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
