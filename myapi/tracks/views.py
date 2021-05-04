from rest_framework import viewsets

from .serializers import TracksSerializer
from .models import Tracks


class TracksViewSet(viewsets.ModelViewSet):
    queryset = Tracks.objects.all().order_by('name')
    serializer_class = TracksSerializer