from django.db import models
from django.contrib.auth.models import User

from django.db import models


class Usuario(models.Model):
    # Definir las opciones de países
    class Nacionalidad(models.TextChoices):
        ARGENTINA = 'AR'
        ESPAÑA = 'ES'
        ITALIA = 'IT'
        FRANCIA = 'FR'
        
    # Conección con User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')

    # Datos del Usuario
    username = models.CharField(max_length=30, blank=True, null=True, unique=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    nacionalidad = models.CharField(
        max_length=2, 
        choices=Nacionalidad.choices, 
        blank=True, 
        null=True
    )
    


    def __str__(self):
        return self.user.username

    
    
    
    
    
    
    
    
    
    


    #perfilprivado = models.BooleanField(default=False)
    #fechadenacimiento = models.DateField(blank=True, null=True)
    #videojuegosfavoritos = models.ManyToManyField()
    

    # Videojuegos
        #videojuego = models.ForeignKey()

    # League of Legends
        #campeonfavoritoslol1 = models.ForeignKey()
        #campeonfavoritolol2 = models.ForeignKey()

    # Counter Strike Global Ofensive 2
        #rolencsgo2 = models.ForeignKey()

    #  Datos de Cuenta
        #fechadecreaciondecuenta = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return f'{self.nombre} {self.apellido} {self.username}' 




# Opciones de videojuegos favoritos
# opciones: lol, csgo2


# Opciones de nacionalidad
# opciones: españa, italia, francia, portugal

# CsGo2
# Opciones de posicion CsGo


# League of Legend
# Opciones de campeones Lol

# Opciones rol en equipo Lol



