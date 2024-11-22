from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def registrarse(request):
    data = request.data
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if User.objects.filter(username=username).exists():
        return Response({"error": "El usuario ya existe"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"success": "Usuario registrado correctamente"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def iniciar_sesion(request):
    data = request.data
    username = data.get("username")
    password = data.get("password")

    user = authenticate(request, username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            "success": "Sesión iniciada",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=status.HTTP_200_OK)
    return Response({"error": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def cerrar_sesion(request):
    logout(request)
    return Response({"success": "Sesión cerrada"}, status=status.HTTP_200_OK)
