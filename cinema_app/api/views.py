from rest_framework import viewsets
from cinema_app.models import Room, Movie
from cinema_app.api.serializers import RoomSerializer, MovieSerializer

class RoomVS(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class MovieVS(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    