from rest_framework import serializers
from cinema_app.models import Room, Movie

class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Room
        exclude = ()
    
class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = Movie
            exclude = ()
