from rest_framework.routers import DefaultRouter
from .views import DatosUsuarioViewSet

router = DefaultRouter()
router.register(r'Usuarios', DatosUsuarioViewSet, basename='DatosUsuario')

urlpatterns = router.urls