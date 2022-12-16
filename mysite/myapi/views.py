from rest_framework import generics, permissions
from .serializers import *
from .models import Content, Channel, Group
    
class ChannelViewSet(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ChannelSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Channel.objects.all()
        fk = self.request.query_params.get('parent_channel', None)
        if fk is not None:
            queryset = queryset.filter(parent_channel=fk)
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

class GroupViewSet(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = GroupSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Group.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

class PlatformViewSet(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CompletePlatformSerializer
    http_method_names = ['get']
    
    def get_queryset(self):
        queryset = Channel.objects.all()
        return queryset


