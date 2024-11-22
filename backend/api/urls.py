from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

router = DefaultRouter()
router.register(r'Usuarios', DatosUsuarioViewSet, basename='DatosUsuario')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='ObtenerToken'),
    path('token/refresh/', TokenRefreshView.as_view(), name='TokenRefresh'),
    path('', include(router.urls)),
    path('accesotoken/', acceso_protegido, name='AccesoProtegido'),
]
