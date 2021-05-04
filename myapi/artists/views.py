from rest_framework import viewsets

from .serializers import ArtistsSerializer
from .models import Artists


class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all().order_by('name')
    serializer_class = ArtistsSerializer