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
from django.utils.crypto import get_random_string
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

def admin_auth(serializer,player_token):
    admin_object = User.objects.get(role='Admin')
    if admin_object.user_token != player_token:
        return False
    else:
        return True
def user_auth(serializer,player_token):
    
    admin_object = User.objects.get(user_token=player_token)
    if admin_object.user_token != player_token:
        return False
    else:
        return True    

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
            data = {"id":user_object[0].id}
            return JsonResponse(data, status=200)
        else:
            return Response(status=403)
    else:
        return Response(status=400)

@api_view(['POST'])
def user_register(request):
    serializer = UserItemSerializer(data=request.data)
    if serializer.is_valid():
        user_object_email = User.objects.filter(email=serializer.initial_data['email'])
        user_object_name = User.objects.filter(name=serializer.initial_data['name'])
        if not user_object_email and not user_object_name:
            serializer.save()
            if serializer.initial_data['name'] == "Martin":
                User.objects.filter(name="Martin").update(role='Admin')
            User.objects.filter(name=serializer.initial_data['name']).update(user_token=get_random_string(length=32))
            return Response(status=200)
        else:
            return Response(status=409)
    else:
        return Response(status=400)


@api_view(['POST'])
def add_training(request,player_token):
    serializer = TrainingItemSerializer(data=request.data)
    if serializer.is_valid():
        if admin_auth(serializer,player_token):

            serializer.save()
            return Response(status=200)
        else:
            return Response(status=401)
        
        
    else:
        return Response(status=400)


@api_view(['POST'])
def training_user(request,player_token):
    serializer = TrainingUserItemSerializer(data=request.data)
    if serializer.is_valid():
        if user_auth(serializer,player_token):

            serializer.save()
            return Response(status=200)
        else:
            return Response(status=401)
    else:
        return Response(status=400)


@api_view(['DELETE'])
def delete_training(request,player_token, id):
    trainings_users = TrainingUser.objects.filter(training=id)
    object = Training.objects.filter(id=id)
    if admin_auth(trainings_users,player_token) == False:
        return Response(status=401)
            
    
        
    if not object:
        return Response(status=400)
    else:
        
        if trainings_users:
            trainings_users.delete()
        object.delete()
        return Response(status=200)
    
    

@api_view(['GET'])
def get_trainings(request,player_token):
    user_object = User.objects.get(user_token=player_token)
    '''
    somarina = {
            "user_token":user_object.user_token,
            "player_token":player_token,
            "user_id":user_object.id
        }
    return Response(somarina,status=404)'''
    if not user_object:
        return Response(status=401)
    
    cursor.execute("SELECT id, title, time, date, CASE WHEN training_id is NULL THEN False ELSE True END as signed_up from trainings LEFT JOIN (SELECT training_id FROM user_training WHERE user_id = %d) x ON trainings.id = training_id ".format(user_object.id))
    record = cursor.fetchone()
    if record == None :
        somarina = {
            "hm":"something wrong"
        }
        return JsonResponse(somarina, status=404)
    print(record)
    training = {
            "id":record[0],
            "title":record[1],
            "time":record[2], 
            "date":record[3],
            "signed_up":record[4]
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
            "date":record[3],
            "signed_up":record[4]
        }
        trainings["training"].append(training)
    
    return JsonResponse(trainings)


@api_view(['GET'])
def get_grouptraining(request,player_token):
    try:
        object = GroupTraining.objects.get()
    except GroupTraining.DoesNotExist:
        return Response(status=404)
    data = {
        "date": object.date,
        "time": object.time,
        "image": object.image
    }
    return JsonResponse(data, status=200)

@api_view(['PUT'])
def put_grouptraining(request,player_token):
    serializer = GroupTrainingItemSerializer(data=request.data)
    if serializer.is_valid():
        if admin_auth(serializer,player_token) == False:
            return Response(status=401)
        data = request.data
        GroupTraining.objects.all().update(date=data['date'], time=data['time'], image=data['image'])
        return Response(status=200)
    else:
        return Response(status=400)

@api_view(['PUT'])
def put_training(request,player_token, id):
    serializer = TrainingTimeItemSerializer(data=request.data)
    if serializer.is_valid():
        if admin_auth(serializer,player_token) == False:
            return Response(status=401)
        data = request.data
        Training.objects.filter(id=id).update(date=data['date'], time=data['time'])
        return Response(status=200)
    else:
        return Response(status=400)



