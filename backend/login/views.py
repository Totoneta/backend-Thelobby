from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json

@csrf_exempt
def Registrarse(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        try:
            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "El usuario ya existe"}, status=400)
            user = User.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({"success": "Usuario registrado correctamente"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def IniciarSesion(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": "Sesión iniciada", "token": "session_active"})
        return JsonResponse({"error": "Credenciales inválidas"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def cerrar_sesion(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"success": "Sesión cerrada"})
    return JsonResponse({"error": "Método no permitido"}, status=405)