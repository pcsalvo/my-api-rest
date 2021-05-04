from rest_framework import viewsets

from .serializers import AlbumsSerializer
from .models import Albums


class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Albums.objects.all().order_by('name')
    serializer_class = AlbumsSerializer