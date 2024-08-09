from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from cinema_app import models


class RoomTestCase(APITestCase):
    
    def setUp(self):
        self.room = models.Room.objects.create(number="2",
                                               description="Testing 2")
    
    def test_room_create(self):
        data={
            "number": "1",
            "description": "Room test"
        }
        response=self.client.post(reverse('room-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_room_list(self):
        response=self.client.get(reverse('room-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_room_detail(self):
        response=self.client.get(reverse('room-detail', args=(self.room.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_room_update(self):
        data={
            "number": "3",
            "description": "Room test"
        }
        response=self.client.put(reverse('room-detail', args=(self.room.id,)), data)
        self.assertEqual(response.data.get("number"), 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
class MovieTestCase(APITestCase):
    
    def setUp(self):
        self.room = models.Room.objects.create(number="1",
                                               description="Testing 1")
        
        self.movie = models.Movie.objects.create(name="Movie 1",
                                                 director= "Director of Movie 1",
                                                 duration="3",
                                                 movie_theater= self.room)
    
    def test_movie_create(self):
        data={
            "name": "Testing123",
            "director": "Director of movie for testing 123",
            "duration": "2",
            "movie_theater": self.room.id
        }
        response=self.client.post(reverse('movies-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_movie_create_without_room(self):
        data={
            "name": "Testing123",
            "director": "Director of movie for testing 123",
            "duration": "2"
        }
        response=self.client.post(reverse('movies-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_movie_list(self):
        response=self.client.get(reverse('movies-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_movie_detail(self):
        response=self.client.get(reverse('movies-detail', args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_movie_update(self):
        data={
            "name": "Testing123",
            "director": "Director of movie for testing 123",
            "duration": "2"
        }
        response=self.client.put(reverse('movies-detail', args=(self.movie.id,)), data)
        self.assertEqual(response.data.get("name"), "Testing123")
        self.assertEqual(response.status_code, status.HTTP_200_OK)