from .models import Usuario 
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import  IsAuthenticated
from django.contrib.auth.models import User


@api_view(['GET', 'PUT'])
def perfil_usuario(request):
    try:
        usuario = request.user.usuario
    except Usuario.DoesNotExist:
        return Response({'detail': 'Perfil no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DatosUsuariosSerializer(usuario)
        print(f"Datos recibidos: {request}")
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DatosUsuariosSerializer(usuario, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    