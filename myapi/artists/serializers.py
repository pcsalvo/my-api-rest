from rest_framework import serializers

from .models import Artists

class ArtistsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artists
        fields = ('name', 'alias')