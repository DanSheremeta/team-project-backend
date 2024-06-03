from django.shortcuts import render
from rest_framework import viewsets
from database.serializers import PetSerializer, DescriptionSerializer, LotSerializer

from database.models import Pet, Description, Lot


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer


class LotViewSet(viewsets.ModelViewSet):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
