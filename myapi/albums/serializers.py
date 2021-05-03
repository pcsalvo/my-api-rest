from rest_framework import serializers

from .models import Albums

class AlbumsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Albums
        fields = ('name', 'alias')