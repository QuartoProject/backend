from rest_framework import serializers
from .models import User, Room, Images_Room, Favorites


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    favorite_rooms = FavoritesSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'


class Images_RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images_Room
        fields = '__all__'

        
class RoomSerializer(serializers.ModelSerializer):
    id_user = UserSerializer(many=False, read_only=True)
    id_images = Images_RoomSerializer(many=False, read_only=True)
    class Meta:
        model = Room
        fields = '__all__'
        