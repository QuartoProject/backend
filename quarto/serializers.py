from rest_framework import serializers
from .models import User, Room, Images_Room, Favorites



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class Images_Room(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

        
class Favorites(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
