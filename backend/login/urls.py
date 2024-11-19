from django.urls import path
from . import views

urlpatterns = [
    path("registrarse/", views.Registrarse, name="Registrarse"),
    path("iniciarsesion/", views.IniciarSesion, name="IniciarSesion"),
]

