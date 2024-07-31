from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema_app.api.views import RoomVS, MovieVS

router = DefaultRouter()
router.register('rooms', RoomVS, basename='room')
router.register('movies', MovieVS, basename='movies')
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
]
