from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room
from .views import RoomView



# enpoint a location on the server that we are going to after the  / 

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer




