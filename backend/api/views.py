from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from rest_framework.response import Response

class CountryViewset(viewsets.ViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Country.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class LeagueViewset(viewsets.ViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = League.objects.all()
        serializer = self.serializer_classerializer(queryset, many=True)
        return Response(serializer.data)
    
class CharacteristicViewset(viewsets.ViewSet):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Characteristic.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

# Create your views here.
