from rest_framework import serializers
from todos import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'lastname',
            'username',
            'email',
            'password',
            'anfitrion',
        )
        model = models.Todo