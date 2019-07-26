from rest_framework import viewsets
from .models import Cliente
from .serializer import ClienteSerializer, LoginSerializer
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente2



class ClienteViewSets(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteLogin(viewsets.ModelViewSet):
    
    queryset = Cliente2.objects.all()
    serializer_class = LoginSerializer


    
    
    
    

    

