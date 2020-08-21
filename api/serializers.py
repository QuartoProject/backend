"""Api serializers."""

# Django modules
from rest_framework import serializers

# Api
from api.models import User, UserProfile, Images_Room, Room, Favorites

"""
Serializers converts the models in python build in data, so that they
can be easily converted to JSON/XML
"""


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('location', 
                  'description', 
                  'phone', 
                  'active', 
                  'favorite_rooms',
                  'picture',
                  )
    
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)
    
    class Meta:
        model = User
        fields = ('url',
                'email',
                'first_name',
                'last_name',
                'password',
                'profile'
                )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user
    
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        
        profile.location = profile_data.get('location', profile.location)
        profile.description = profile_data.get('description', profile.description)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.active = profile_data.get('active', profile.active)
        profile.favorite_rooms = profile_data.get('favorite_rooms', profile.favorite_rooms)
        profile.picture = profile_data.get('picture', profile.picture)
        profile.save()
        
        return instance


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
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