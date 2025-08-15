from django.urls import path, include
from . import views
from .views import *

from rest_framework.routers import DefaultRouter

from .views import AmistadViewSet, UsuariosViewSet


# Instancia del router
router = DefaultRouter()

# Registrar los viewsets
router.register(r'amistades', AmistadViewSet, basename='AmistadEntreUsuarios')
router.register(r'usuarios', UsuariosViewSet, basename='ListaUsuarios')

urlpatterns = [
    path('perfil/', views.perfil_usuario, name='PerfilUsuario'),
    
    path('amistades/<int:pk>/enviar_solicitud/', AmistadViewSet.as_view({'post': 'enviar_solicitud'}), name='enviar_solicitud'),
    path('amistades/<int:pk>/aceptar_solicitud/', AmistadViewSet.as_view({'post': 'aceptar_solicitud'}), name='aceptar_solicitud'),
    path('amistades/<int:pk>/rechazar_solicitud/', AmistadViewSet.as_view({'post': 'rechazar_solicitud'}), name='rechazar_solicitud'),
    path('amistades/solicitudespendientes/', solicitudes_pendientes, name='solicitudes_pendientes'),

    path('', include(router.urls)),
]
