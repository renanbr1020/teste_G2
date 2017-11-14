from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from frequencia.models import *
from frequencia.serializers import *


# Create your views here.

class TipoRegistroViewSet(viewsets.ModelViewSet):
    queryset = TipoRegistro.objects.all()
    serializer_class = TipoRegistroSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

