from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import psycopg2
import os
from django.http import HttpResponse
from .serializers import *
from .models import *
import json


@api_view(['POST'])
def add_user(request):
    print("hello")
    api_key = request.GET.get('api_key')
    #serializer = UserItemSerializer(data=request.data)
    #if serializer.is_valid():
        #serializer.save()
    #else:
        #print("Not good")

@api_view(['GET'])
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


