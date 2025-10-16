from rest_framework import serializers
from .models import Usuario, Amistad

#datos del usuario
class DatosUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'nacionalidad', 'username', 'juegoprimero', 'juegoprimeronivel']

#solicitudes de amistad
class AmistadSerializer(serializers.ModelSerializer):
    usuario1_id = serializers.CharField(source='usuario1.id', read_only=True)
    usuario2_id = serializers.CharField(source='usuario2.id', read_only=True)
    usuario1_username = serializers.CharField(source='usuario1.username', read_only=True)
    usuario2_username = serializers.CharField(source='usuario2.username', read_only=True)
    
    class Meta:
        model = Amistad
        fields = ['usuario1_id', 'usuario2_id', 'usuario1_username', 'usuario2_username', 'estado', 'fecha_solicitud']