from django.urls import path
from . import views

urlpatterns = [
    path("registrarse/", views.registrarse, name="Registrarse"),
    path("iniciarsesion/", views.iniciar_sesion, name="IniciarSesion"),
    path("cerrarsesion/", views.cerrar_sesion, name="CerrarSesion"),
]

