from rest_framework import serializers

from .models import Content, Channel

class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = ('title', 'desc', 'author', 'genere', 'rating')

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ('title', 'language')

class CompletePlatformSerializer(serializers.HyperlinkedModelSerializer):
    contents = ContentSerializer(many = True)
    subchannels = ChannelSerializer(many = True)

    class Meta:
        model = Channel
        fields = ('title', 'language', 'subchannels', 'contents')
