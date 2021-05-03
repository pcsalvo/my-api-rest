from rest_framework import serializers

from .models import Tracks

class TracksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tracks
        fields = ('name', 'alias')