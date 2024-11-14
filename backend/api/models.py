from django.db import models


# PLAYERS
class Player(models.Model):
    # Datos del player
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
    fechadenacimiento = models.DateField(blank=True, null=True)
    posicionglobal = models.IntegerField(blank=True, null=True)

    # Stats
    adr = models.FloatField(blank=True, null=True)
    kda = models.FloatField(blank=True, null=True)
    headshots = models.FloatField(blank=True, null=True)
    dpr = models.FloatField(blank=True, null=True)
    wr = models.FloatField(blank=True, null=True)
    kast = models.FloatField(blank=True, null=True)

    #nacionalidad = models.IntegerChoices(blank=True, null=True) # Rellenar con opciones

#class PosicionamientoEnEquipo ():

#class Nacionalidad ():

#class Videojuegos ():

#class Equipos ():

#class CampeonesLol():

#class ArmasCsGo():

#class RolDeEquipoCsgo():

#class RolDeEquipoLol():

    # Relacion entre clases
    #videojuego = models.ForeignKey()
    #equipoactual = models.ForeignKey()
    #equiposdecarrera = models.ManyToManyField()
    #fechadeingresoalequipoactual = models.DateField()
    #campeonfavoritouno = models.ForeignKey()
    #campeonfavoritodos = models.ForeignKey()
    #campeonfavoritotres = models.ForeignKey()
    #armafavorita = models.ForeignKey()
    #roldeequipo = models.ForeignKey()


    def __str__(self):
        return f'{self.nombre} {self.username} {self.videojuego} {self.equipoactual}'

