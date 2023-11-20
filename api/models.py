from django.db import models
from django.utils import timezone



class Programmer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

def get_current_date():
    return timezone.now().date()

class Tickets(models.Model):
    nombrecliente = models.CharField(max_length=100)
    fecha = models.DateField(default=get_current_date)
    descripcion = models.CharField(max_length=500)
    abierto = models.BooleanField(default=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pagado', 'Pagado'),
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        # Otros estados que puedan existir
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    client = models.CharField(max_length=100)
    order_number = models.CharField(max_length=20)
    date = models.DateField(default=get_current_date)  
