from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import psycopg2
import os
from django.http import HttpResponse
import json


@api_view(['POST'])
def add_training(request, id):
    print("hello")
    api_key = request.GET.get('api_key')


