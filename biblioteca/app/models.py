from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    pais_origem = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome # Exibe o nome no Admin do Django

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    # ForeignKey cria a relação 1-N (Um autor tem vários livros)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    data_publicacao = models.DateField()
    isbn = models.CharField(max_length=13, unique=True) # ISBN único por livro

    def __str__(self):
        return self.titulo
