from django.shortcuts import render
from rest_framework import viewsets
from app.serializers import Pet_informationSerializer, DescriptionSerializer

from app.models import Pet_information, Description


class Pet_informationViewSet(viewsets.ModelViewSet):
    queryset = Pet_information.objects.all()
    serializer_class = Pet_informationSerializer


class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
