from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.Choices('Admin', 'User')
    group_training = models.BooleanField()
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
    gym_id = models.ForeignKey(Gym, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'coach'

class Training(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField()
    coach_id = models.ForeignKey(Coach, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'trainings'


class TrainingUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    training_id = models.ForeignKey(Training, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_training'


class GroupTraining(models.Model):
    #user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'group_training'



