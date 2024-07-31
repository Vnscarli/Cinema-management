from django.db import models

class Room(models.Model):
    number = models.IntegerField()
    description = models.CharField(max_length=150)
    

class Movie(models.Model):
    name = models.CharField(max_length=60)
    director = models.CharField(max_length=60)
    duration = models.IntegerField()
    movie_theater = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name="movies")