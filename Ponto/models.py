from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from Categoria.models import Categoria
# Create your models here.

@python_2_unicode_compatible
class Ponto(models.Model):

    INITIAL_ID = 1

    id_ponto = models.IntegerField(default=INITIAL_ID)
    nomePonto = models.CharField(max_length=150)
    descricao = models.CharField(max_length=700)
    resumo = models.CharField(max_length=350)
    distancia = models.FloatField()
    duracao = models.FloatField()
    desnivel = models.FloatField()
    dificuldade = models.CharField(max_length=10)
    coordenada_X = models.FloatField()
    coordenada_Y = models.FloatField()
    categoria = models.ForeignKey(Categoria, default=INITIAL_ID, on_delete=models.CASCADE)


    def __str__(self):
        return self.nomePonto
