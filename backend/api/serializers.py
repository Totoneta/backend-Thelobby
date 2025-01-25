from rest_framework import serializers
from .models import Usuario

class DatosUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'nacionalidad']
