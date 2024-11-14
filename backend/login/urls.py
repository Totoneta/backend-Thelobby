from django.urls import path
from .views import IniciarSesion, Registrarse



urlpatterns = [
    path('iniciarsesion/', IniciarSesion.as_view(), name='IniciarSesion'),
    path('registrarse/', Registrarse, name='Registrarse'),
]
