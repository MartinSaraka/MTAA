from rest_framework import serializers
from .models import User

class UserItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    group_training = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('__all__')
