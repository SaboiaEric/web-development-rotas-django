from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
# Create your models here.

@python_2_unicode_compatible
class Categoria(models.Model):

    INITIAL_ID = 1

    id_categoria = models.IntegerField(default=INITIAL_ID)
    nomeCategoria = models.CharField(max_length=150)
    descricao = models.CharField(max_length=350)



    def __str__(self):
        return self.nomeCategoria
