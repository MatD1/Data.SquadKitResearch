from django.shortcuts import render
from rest_framework import viewsets
from Weapons.models import AustralianArmyWeapons
from Weapons.serializers import AustralianArmyWeaponsSerializer

# Create your views here.
class AustralianArmyWeaponsViewSet(viewsets.ModelViewSet):
    queryset = AustralianArmyWeapons.objects.all().order_by('Weapon')
    serializer_class = AustralianArmyWeaponsSerializer