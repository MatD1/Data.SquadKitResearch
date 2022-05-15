from django.shortcuts import render

from rest_framework import viewsets
from .serializers import AustralianArmySerializer, BritishSerializer, CanadianArmySerializer, InsurgentSerializer, IrregularMilitiaSerializer, MiddleEasterAllianceSerializer, PanAsiaSerializer, PostSerializer, RussianGroundForcesSerializer, UnitedStatesArmySerializer, UnitedStatesMarineCoreSerializer
from .models import AustralianArmy, British, CanadianArmy, IrregularMilitia, Post, Insurgent, MiddleEasternAlliance, PanAsia, RussianGroundForces, UnitedStatesArmy, UnitedStatesMarineCore
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('name')
    serializer_class = PostSerializer

class InsurgentViewSet(viewsets.ModelViewSet):
    queryset = Insurgent.objects.all().order_by('RoleName')
    serializer_class = InsurgentSerializer

class BritishViewSet(viewsets.ModelViewSet):
    queryset = British.objects.all().order_by('RoleName')
    serializer_class = BritishSerializer

class AustralianArmyViewSet(viewsets.ModelViewSet):
    queryset = AustralianArmy.objects.all().order_by('RoleName')
    serializer_class = AustralianArmySerializer

class CanadianArmyViewSet(viewsets.ModelViewSet):
    queryset = CanadianArmy.objects.all().order_by('RoleName')
    serializer_class = CanadianArmySerializer

class IrregularMilitiaViewSet(viewsets.ModelViewSet):
    queryset = IrregularMilitia.objects.all().order_by('RoleName')
    serializer_class = IrregularMilitiaSerializer

class MiddleEasternAllianceViewSet(viewsets.ModelViewSet):
    queryset = MiddleEasternAlliance.objects.all().order_by('RoleName')
    serializer_class = MiddleEasterAllianceSerializer

class PanAsiaViewSet(viewsets.ModelViewSet):
    queryset = PanAsia.objects.all().order_by('RoleName')
    serializer_class = PanAsiaSerializer

class RussianGroundForcesViewSet(viewsets.ModelViewSet):
    queryset = RussianGroundForces.objects.all().order_by('RoleName')
    serializer_class = RussianGroundForcesSerializer

class UnitedStatesArmyViewSet(viewsets.ModelViewSet):
    queryset = UnitedStatesArmy.objects.all().order_by('RoleName')
    serializer_class = UnitedStatesArmySerializer

class UnitedStatesMarineCoreViewSet(viewsets.ModelViewSet):
    queryset = UnitedStatesMarineCore.objects.all().order_by('RoleName')
    serializer_class = UnitedStatesMarineCoreSerializer




















