from rest_framework import serializers
from .models import Funcionario, Curso 

# O Serializer do Curso precisa vir primeiro ou ser independente
class CursoSerializer(serializers.ModelSerializer):
    """
    Este serializer transforma os dados da tabela Curso do MySQL para JSON.
    Ele será usado tanto para a API de Cursos quanto para aparecer 
    dentro da API de Funcionários.
    """
    class Meta:
        model = Curso
        # O '__all__' indica que queremos enviar ID, Nome e Carga Horária para o Postman
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    """
    Este é o serializer principal. Ele busca os dados do Funcionário 
    e gerencia a relação Many-to-Many com a tabela de Cursos.
    """
    class Meta:
        model = Funcionario
        # Aqui ele pega: Nome, Cargo, Data, Salário e a lista de IDs dos Cursos
        fields = '__all__'