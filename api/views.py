from rest_framework import viewsets
from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer

class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

class ClienteCountView(APIView):
    def get(self, request):
        # Obtener el recuento de registros en la tabla Programmer
            count = Cliente.objects.count()
            return Response({'count': count})

class TicketsAbiertosCountView(APIView):
    def get(self, request):
        # Obtener el recuento de registros con 'abierto' en True
        count_abiertos = Tickets.objects.filter(abierto=True).count()
        return Response({'count_abiertos': count_abiertos})

class TicketsCerradosCountView(APIView):
    def get(self, request):
        # Obtener el recuento de registros con 'abierto' en False
        count_cerrados = Tickets.objects.filter(abierto=False).count()
        return Response({'count_cerrados': count_cerrados})

class ProgrammerCountView(APIView):
    def get(self, request):
        # Obtener el recuento de registros en la tabla Programmer
            count = Programmer.objects.count()
            return Response({'count': count})

class OrderCountView(APIView):
    def get(self, request):
        # Obtener el recuento de registros en la tabla Programmer
            count = Order.objects.count()
            return Response({'count': count})