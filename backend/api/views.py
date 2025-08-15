from .models import Usuario 
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

#Solicitudes de amistad entre usuarios
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Amistad
from .serializers import AmistadSerializer

#Obtener datos del usuario iniciado y editar sus datos
@api_view(['GET', 'PUT'])
def perfil_usuario(request):
    try:
        usuario = request.user.usuario
    except Usuario.DoesNotExist:
        return Response({'detail': 'Perfil no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DatosUsuariosSerializer(usuario)
        print(f"Datos recibidos: {request.data}")
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DatosUsuariosSerializer(usuario, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------------------

#Mostrar todos los usuarios
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = DatosUsuariosSerializer
    permission_classes = [IsAuthenticated]
    
    # Acción para obtener todos los usuarios
    @action(detail=False, methods=['get'])
    def lista_usuarios(self, request):
        usuarios = Usuario.objects.all()
        serializer = DatosUsuariosSerializer(usuarios, many=True)
        return Response(serializer.data)

# -------------------------------------------------------------

#Amistad entre Usuarios
class AmistadViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    # Enviar solicitud de amistad
    @action(detail=True, methods=['post'])
    def enviar_solicitud(self, request, pk=None):
        usuario_recibido = Usuario.objects.get(pk=pk)
        usuario_actual = request.user.usuario  # Obtienes el usuario actual de la sesión

        if usuario_actual == usuario_recibido:
            return Response({"detail": "No puedes enviarte una solicitud a ti mismo."}, status=status.HTTP_400_BAD_REQUEST)

        if Amistad.objects.filter(usuario1=usuario_actual, usuario2=usuario_recibido, estado='pendiente').exists():
            return Response({"detail": "Ya has enviado una solicitud de amistad."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Crear la solicitud de amistad
        amistad = Amistad.objects.create(usuario1=usuario_actual, usuario2=usuario_recibido)
        return Response({"detail": "Solicitud de amistad enviada."}, status=status.HTTP_200_OK)

    # -------------------------------------------------------------

    # Aceptar solicitud de amistad
    @action(detail=True, methods=['post'])
    def aceptar_solicitud(self, request, pk=None):
        usuario_actual = request.user.usuario
        solicitud = Amistad.objects.filter(usuario2=usuario_actual, usuario1__id=pk, estado='pendiente').first()

        if not solicitud:
            return Response({"detail": "No tienes una solicitud pendiente de este usuario."}, status=status.HTTP_400_BAD_REQUEST)

        solicitud.estado = 'aceptada'
        solicitud.save()
        return Response({"detail": "Solicitud de amistad aceptada."}, status=status.HTTP_200_OK)

    # -------------------------------------------------------------

    # Rechazar solicitud de amistad
    @action(detail=True, methods=['post'])
    def rechazar_solicitud(self, request, pk=None):
        usuario_actual = request.user.usuario
        solicitud = Amistad.objects.filter(usuario2=usuario_actual, usuario1__id=pk, estado='pendiente').first()

        if not solicitud:
            return Response({"detail": "No tienes una solicitud pendiente de este usuario."}, status=status.HTTP_400_BAD_REQUEST)

        solicitud.estado = 'rechazada'
        solicitud.save()
        return Response({"detail": "Solicitud de amistad rechazada."}, status=status.HTTP_200_OK)
    
    # -------------------------------------------------------------

    # Obtener los amigos
    @action(detail=False, methods=['get'])
    def amistades(self, request):
        usuario_actual = request.user.usuario
        
        amistades = Amistad.objects.filter(
            (Q(usuario1=usuario_actual) | Q(usuario2=usuario_actual)),
            estado='aceptada'
        )
        
        amigos = []
        for amistad in amistades:
            if amistad.usuario1 == usuario_actual:
                amigos.append(amistad.usuario2)
            else:
                amigos.append(amistad.usuario1)
        
        # Serializar la lista de amigos
        serializer = DatosUsuariosSerializer(amigos, many=True)
        return Response(serializer.data)

# -------------------------------------------------------------

from django.db.models import Q

# Ver solicitudes pendientes
@api_view(['GET'])
def solicitudes_pendientes(request):
    try:
        usuario_actual = request.user.usuario
    except AttributeError:
        return Response({"detail": "Usuario no autenticado"}, status=status.HTTP_401_UNAUTHORIZED)


    solicitudes = Amistad.objects.filter(
        usuario2=usuario_actual,
        estado='pendiente'
    )

    if not solicitudes.exists():
        return Response({"detail": "No tienes solicitudes pendientes."}, status=status.HTTP_200_OK)

    serializer = AmistadSerializer(solicitudes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# -------------------------------------------------------------
