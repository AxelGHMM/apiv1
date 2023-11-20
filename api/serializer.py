from rest_framework import serializers
from .models import *

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Programmer
        fields='__all__'

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tickets
        fields='__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'