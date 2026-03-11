from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, LivroViewSet

# O Router cria rotas como /autores/ e /livros/ sozinho
router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]