from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import Content, Channel

class PlatformViewSet(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CompletePlatformSerializer
    http_method_names = ['get']
    
    def get_queryset(self):
        queryset = Channel.objects.all()
        return queryset
    
    
class ChannelViewSet(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ChannelSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Channel.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset

class ContentViewSet(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ContentSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Content.objects.all()
        fk = self.request.query_params.get('parent_channel', None)
        if fk is not None:
            queryset = queryset.filter(parent_channel=fk)
        return queryset


