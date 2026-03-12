from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, FuncionarioViewSet

# Criamos o roteador que vai gerenciar as URLs automaticamente
router = DefaultRouter()

# Registramos as rotas. 
# O primeiro parâmetro é o nome que aparecerá na URL (ex: api/funcionarios/)
router.register(r'cursos', CursoViewSet)
router.register(r'funcionarios', FuncionarioViewSet)

# As URLs da API agora estão contidas no roteador
urlpatterns = [
    path('', include(router.urls)),
]