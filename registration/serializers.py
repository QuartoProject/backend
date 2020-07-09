from rest_framework import serializers
from quarto.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'lastname', 'username', 'email')

"""
Register
"""
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'lastname', 'username', 'email', 'password', 'anfitrion')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_new = User(name=validated_data['name'], lastname=validated_data['lastname'], username=validated_data['username'], email=validated_data['email'], password=validated_data['password'], anfitrion=validated_data['anfitrion'],active=True)
        user_new.save()
        return user_new
    

"""
Serializer to change password
"""
class ChangePasswordSerializer(serializers.Serializer):
    model = User
    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    