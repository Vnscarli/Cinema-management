from django.db import models

class Room(models.Model):
    number = models.IntegerField()
    description = models.CharField(max_length=150)
    
    def __str__(self):
        return str(self.description)
    

class Movie(models.Model):
    name = models.CharField(max_length=60)
    director = models.CharField(max_length=60)
    duration = models.IntegerField()
    movie_theater = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name="movies")
    
    def __str__(self):
        return self.name
    