from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .models import Cliente

from .serializer import LoginSerializer

@csrf_exempt

def Login(request,cedula):
    cliente = Cliente.objects.filter(cedula=cedula)

    if request.method == 'GET':
        serializer_class = LoginSerializer
