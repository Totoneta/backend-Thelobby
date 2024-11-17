from rest_framework import serializers
from login.models import Usuario

class DatosUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'