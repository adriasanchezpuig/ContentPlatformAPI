from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ContentSerializer, ChannelSerializer
from .models import Content, Channel
# Create your views here.

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all().order_by('title')
    serializer_class = ContentSerializer

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all().order_by('title')
    serializer_class = ChannelSerializer