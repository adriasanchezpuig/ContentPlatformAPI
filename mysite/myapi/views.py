from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import Content, Channel

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
        pk = self.request.query_params.get('id', None)
        if pk is not None:
            queryset = queryset.filter(id=pk)
        return queryset


