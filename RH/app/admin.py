from django.contrib import admin

# Primeiro, importe os modelos que você criou
from .models import Curso, Funcionario 

# Depois, registre cada um deles
admin.site.register(Curso)
admin.site.register(Funcionario)
