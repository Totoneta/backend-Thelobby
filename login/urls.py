from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("registrarse/", views.registrarse, name="Registrarse"),
    path("iniciarsesion/", views.iniciar_sesion, name="IniciarSesion"),
    path("cerrarsesion/", views.cerrar_sesion, name="CerrarSesion"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

