from rest_framework import serializers
from .models import Cliente, Cliente2
from rest_framework.fields import CurrentUserDefault

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = ('nombre','cedula')


       
            