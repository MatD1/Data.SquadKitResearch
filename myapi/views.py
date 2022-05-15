from django.shortcuts import render

from rest_framework import viewsets
from .serializers import BritishSerializer, InsurgentSerializer, PostSerializer
from .models import British, Post, Insurgent
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