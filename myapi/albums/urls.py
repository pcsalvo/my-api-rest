from django.urls import path
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'albums', views.AlbumsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

#urlpatterns = [
    #path('<str:album_id>/', ),
    #path('<str:album_id>/tracks/', ),
    #path('<str:album_id>/tracks/play/', )
#]