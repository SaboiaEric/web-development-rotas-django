from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.

@python_2_unicode_compatible
class Cidade(models.Model):

    INITIAL_ID = 1

    nomeCidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    id_cidade = models.IntegerField(default=INITIAL_ID)

    def __str__(self):
        return self.nomeCidade
