from django.shortcuts import render

from rest_framework import viewsets
from .models import Curso, Funcionario
from .serializers import CursoSerializer, FuncionarioSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all() # Busca todos os cursos no MySQL
    serializer_class = CursoSerializer # Usa o tradutor que criamos

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
