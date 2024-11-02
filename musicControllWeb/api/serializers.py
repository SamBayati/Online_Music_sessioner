## this serializer class is suppoised to take all the entities of the model in the models.py class and give it to the front end in the form of JSON
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Room
    # Id is the primary key for each of the models so each of them can be deffrenciate
        fields = ('id','code','host','guest_can_pause','votes_to_skip','created_at')