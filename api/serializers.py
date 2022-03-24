from rest_framework import serializers
from .models import Coach, Training, User, TrainingUser, GroupTraining


class UserItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    group_training = serializers.BooleanField()

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'group_training']


class CoachItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)

    class Meta:
        model = Coach
        fields = ['name']


class TrainingItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    time = serializers.DateTimeField()
    coach_id = serializers.IntegerField()

    class Meta:
        model = Training
        fields = ['name', 'title', 'time', 'coach_id']


class TrainingUserItemSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    training_id = serializers.IntegerField()

    class Meta:
        model = TrainingUser
        fields = ['user_id', 'training_id']


class GroupTrainingItemSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField()

    class Meta:
        model = GroupTraining
        fields = ['time']