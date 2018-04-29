from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from Categoria.models import Categoria
from Ponto.models import Ponto

# Create your models here.

@python_2_unicode_compatible
class Rota(models.Model):

    INITIAL_ID = 1

    id_rota = models.IntegerField(default=INITIAL_ID)
    nomeRota = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, default=INITIAL_ID, on_delete=models.CASCADE)
    pontos = models.ManyToManyField(Ponto)

    def __str__(self):
        return self.nomeRota
