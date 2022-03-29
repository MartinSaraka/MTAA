from rest_framework import serializers
from .models import Coach, Training, User, TrainingUser, GroupTraining


class UserItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)    
    class Meta:
        model = User
        fields = ['name', 'email', 'password',]


class CoachItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)

    class Meta:
        model = Coach
        fields = ['name']


class TrainingItemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    time = serializers.TimeField()
    date = serializers.DateField()
    coach = serializers.PrimaryKeyRelatedField(queryset=Coach.objects.all())

    class Meta:
        model = Training
        fields = ['title', 'time', 'date', 'coach']


class TrainingUserItemSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    training = serializers.PrimaryKeyRelatedField(queryset=Training.objects.all())

    class Meta:
        model = TrainingUser
        fields = ['user', 'training']


class GroupTrainingItemSerializer(serializers.ModelSerializer):
    time = serializers.TimeField()
    date = serializers.DateField()
    image = serializers.CharField()

    class Meta:
        model = GroupTraining
        fields = ['time', 'date', 'image']


class UserLoginItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['name', 'password']


class TrainingTimeItemSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    time = serializers.TimeField()

    class Meta:
        model = Training
        fields = ['date', 'time']
