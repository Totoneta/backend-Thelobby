from rest_framework.viewsets import ModelViewSet
from login.models import Usuario 
from .serializers import DatosUsuariosSerializer

class DatosUsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = DatosUsuariosSerializer