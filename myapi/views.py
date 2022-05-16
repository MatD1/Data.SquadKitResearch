from encodings import search_function
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import AustralianArmySerializer, BritishSerializer, CanadianArmySerializer, InsurgentSerializer, IrregularMilitiaSerializer, MiddleEasterAllianceSerializer, PanAsiaSerializer, PostSerializer, RussianGroundForcesSerializer, UnitedStatesArmySerializer, UnitedStatesMarineCoreSerializer
from .models import AustralianArmy, British, CanadianArmy, IrregularMilitia, Post, Insurgent, MiddleEasternAlliance, PanAsia, RussianGroundForces, UnitedStatesArmy, UnitedStatesMarineCore
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('name')
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class InsurgentViewSet(viewsets.ModelViewSet):
    queryset = Insurgent.objects.all().order_by('id')
    serializer_class = InsurgentSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class BritishViewSet(viewsets.ModelViewSet):
    queryset = British.objects.all().order_by('id')
    serializer_class = BritishSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class AustralianArmyViewSet(viewsets.ModelViewSet):
    queryset = AustralianArmy.objects.all().order_by('id')
    serializer_class = AustralianArmySerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class CanadianArmyViewSet(viewsets.ModelViewSet):
    queryset = CanadianArmy.objects.all().order_by('id')
    serializer_class = CanadianArmySerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class IrregularMilitiaViewSet(viewsets.ModelViewSet):
    queryset = IrregularMilitia.objects.all().order_by('id')
    serializer_class = IrregularMilitiaSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class MiddleEasternAllianceViewSet(viewsets.ModelViewSet):
    queryset = MiddleEasternAlliance.objects.all().order_by('id')
    serializer_class = MiddleEasterAllianceSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class PanAsiaViewSet(viewsets.ModelViewSet):
    queryset = PanAsia.objects.all().order_by('id')
    serializer_class = PanAsiaSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class RussianGroundForcesViewSet(viewsets.ModelViewSet):
    queryset = RussianGroundForces.objects.all().order_by('id')
    serializer_class = RussianGroundForcesSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class UnitedStatesArmyViewSet(viewsets.ModelViewSet):
    queryset = UnitedStatesArmy.objects.all().order_by('id')
    serializer_class = UnitedStatesArmySerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']

class UnitedStatesMarineCoreViewSet(viewsets.ModelViewSet):
    queryset = UnitedStatesMarineCore.objects.all().order_by('id')
    serializer_class = UnitedStatesMarineCoreSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['RoleName', 'id']
    filterset_fields = ['RoleName', 'id']




















