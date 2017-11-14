from django.db import models

from django.contrib.auth.models import User
from django import forms

class Horario (models.Model):
    hora = models.CharField(max_length=40)
    def __str__ (self):
        return self.hora

class Funcionario (models.Model):
    nome = models.CharField(max_length=40)
    horario = models.ManyToManyField(Horario)
    def __str__ (self):
        return self.nome

class TipoRegistro (models.Model):
    nome_registro = models.CharField(max_length=8)
    def __str__ (self):
        return self.nome_registro

class Frequencia(models.Model):
    tipo_registro = models.ForeignKey(TipoRegistro)
    chefe = models.CharField(max_length=40)
    ipMaquina = models.CharField(max_length=20)
    dataHora = models.DateTimeField(blank=False, null=False)

    funcionario = models.ForeignKey(Funcionario)
    
    consistente = models.BooleanField("Está pontual?",default=False)
    inconsistente = models.BooleanField("Está atrasado?",default=False)
    justificativa = models.TextField()
    

    def __str__ (self):
        return "Funcionário: "+self.funcionario.nome
