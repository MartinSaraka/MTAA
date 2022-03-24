from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import psycopg2
import os
from django.http import HttpResponse, JsonResponse
from .serializers import *
from .models import *
import json
import environ
env = environ.Env()
environ.Env.read_env()

# Connect to an existing database
connection = psycopg2.connect(
        dbname = env('DB_NAME'),
        user = env('DB_USER'),
        password = env('DB_PASSWORD'),
        host = "localhost",
        port = "5432")

cursor = connection.cursor()


@api_view(['POST'])
def add_user(request):
    print("hello")
    api_key = request.GET.get('api_key')
    #serializer = UserItemSerializer(data=request.data)
    #if serializer.is_valid():
        #serializer.save()
    #else:
        #print("Not good")

@api_view(['POST'])
def user_login(request):
    serializer = UserLoginItemSerializer(data=request.data)
    if serializer.is_valid():
        user_object = User.objects.filter(name=serializer.initial_data['name'], password=serializer.initial_data['password'])
        if user_object:
            return Response(status=200)
        else:
            return Response(status=400)
    else:
        return Response(status=405)

@api_view(['POST'])
def user_register(request):
    serializer = UserItemSerializer(data=request.data)
    if serializer.is_valid():
        user_object = User.objects.filter(email=serializer.initial_data['email'])
        if not user_object:
            serializer.save()
            return Response(status=200)
        else:
            return Response(status=402)
    else:
        return Response(status=405)


@api_view(['POST'])
def add_training(request):
    serializer = TrainingItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200)
    else:
        return Response(status=405)


@api_view(['POST'])
def training_user(request):
    serializer = TrainingUserItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200)
    else:
        return Response(status=405)


@api_view(['DELETE'])
def delete_training(request, id):
    trainings_users = TrainingUser.objects.get(training=id)
    object = Training.objects.get(id=id)
    if not object:
        return Response(status=404)
    else:
        trainings_users.delete()
        object.delete()
        return Response(status=200)
    
    

@api_view(['GET'])
def get_trainings(request):
    
    cursor.execute("SELECT * from trainings")
    
    
    record = cursor.fetchone()
    if record == None :
        somarina = {
            "hm":"Ic do pici"
        }
        return JsonResponse(somarina)
    print(record)
    training = {
            "id":record[0],
            "title":record[1],
            "time":record[2], 
            "date":record[3]
        }
    trainings = {
            "training":[training]
        } 
    
    while record != None:
        record = cursor.fetchone()
        if record == None:
            break
        training = {
            "id":record[0],
            "title":record[1],
            "time":record[2],
            "date":record[3]
        }
        trainings["training"].append(training)
    
    return JsonResponse(trainings)     