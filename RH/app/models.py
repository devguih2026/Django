from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    # Opcional: Útil para o RH saber a qualificação do funcionário
    carga_horaria = models.IntegerField(help_text="Duração em horas", default=0)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    contratacao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    cursos = models.ManyToManyField(Curso, related_name="funcionarios")

    def __str__(self):
        return self.nome
    

