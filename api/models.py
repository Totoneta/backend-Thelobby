from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    
    # Definir las opciones de países
    class Nacionalidad(models.TextChoices):
        ARGENTINA = 'AR'
        ESPAÑA = 'ES'
        ITALIA = 'IT'
        FRANCIA = 'FR'

    # Definir las opciones de juegos
    class Juegos(models.TextChoices):
        csgo2 = 'CSGO2'
        rocketleague = 'ROCKETLEAGUE'
        gtav = 'GTAV'
        minecraft = 'MINECRAFT'
        dst = 'DONTSTARVETOGETHER'
        fifa = 'FIFA'
        fortnite = 'FORTNITE'
        rainbow6 = 'RAINBOW6'
        
    # Conección con User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
    
    # Datos del Usuario
    username = models.CharField(max_length=40, blank=False, null=False, name='username', default='')
    nombre = models.CharField(max_length=40, blank=False, null=False, name='nombre')
    nacionalidad = models.CharField(  
        max_length=20,
        choices=Nacionalidad.choices, 
        blank=False, 
        null=False,
        default='AR',
    )
    juegoprimero = models.CharField( 
        max_length=20,
        choices=Juegos.choices,
        blank=False,
        null=False,
        default='CSGO2'
    )

    juegoprimeronivel = models.CharField(max_length=50, blank=False, null=False, name='juegoprimeronivel', default='')

    def __str__(self):
        return self.user.username


class Amistad(models.Model):
    # Relacionar usuarios
    usuario1 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="amistades_iniciadas")
    usuario2 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="amistades_recibidas")
    
    # Estado de la amistad (pendiente, aceptada, rechazada)
    ESTADO_AMISTAD = (
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
    )
    
    estado = models.CharField(
        max_length=10, 
        choices=ESTADO_AMISTAD, 
        default='pendiente'
    )
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Amistad entre {self.usuario1.user.username} y {self.usuario2.user.username} - {self.estado}"
