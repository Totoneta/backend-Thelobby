from django.db import models
from django.contrib.auth.models import User
from api.models import Player


# USER DATA
class Usuario(models.Model):
    #Conección con User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #Datos del Usuario
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
    fechadenacimiento = models.DateField(blank=True, null=True)


#class TipoDocumento(): # Dni, Pasaporte, etc

    # Datos de Cuenta
    #fechadecreaciondecuenta = models.DateTimeField(auto_now_add=True)

    # Modelos de Api
    #nacionalidad = models.IntegerChoices(blank=True, null=True) # Rellenar con opciones
    #videojuegosfavoritos = models.ManyToManyField()
    #playersfavoritos = models.ManyToManyField()
    #equiposfavoritos = models.ManyToManyField()

    # Seguridad
    #tipodocumento = models.IntegerChoices()
    #document = models.IntegerField()
    


