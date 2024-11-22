from login.models import Usuario 
from .serializers import DatosUsuariosSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class DatosUsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = DatosUsuariosSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def acceso_protegido(request):
    return Response({'message': 'Acceso autorizado, datos protegidos.'})
