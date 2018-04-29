from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from Cidade.models import Cidade
from Categoria.models import Categoria

@python_2_unicode_compatible
class Usuario(models.Model):

    INITIAL_ID = 1
    
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=100)
    CPF = models.CharField(max_length=15)
    local_x = models.CharField(max_length=100)
    local_y = models.CharField(max_length=100)
    id_usuario = models.IntegerField(default=INITIAL_ID)
    cidades = models.ManyToManyField(Cidade)
    categoria = models.ForeignKey(Categoria, default=INITIAL_ID, on_delete=models.CASCADE)

    def __str__(self):
        return (self.nome)