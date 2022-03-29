from django.db import models
from datetime import date
import django.utils.timezone
from django.utils.crypto import get_random_string


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200, default="User")
    user_token = models.CharField(max_length=200, default=get_random_string(length=32))
    group_training = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'


class Gym(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'gym'


class Coach(models.Model):
    name = models.CharField(max_length=200)
    gym = models.ForeignKey(Gym, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'coach'


class Training(models.Model):
    title = models.CharField(max_length=200)
    time = models.TimeField()
    date = models.DateField(default=django.utils.timezone.now)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'trainings'


class TrainingUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    training = models.ForeignKey(Training, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_training'


class GroupTraining(models.Model):
    #user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time = models.TimeField()
    date = models.DateField(default=django.utils.timezone.now)
    image = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'group_training'



