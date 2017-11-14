from rest_framework import routers, serializers, viewsets
from frequencia.models import *


class TipoRegistroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoRegistro
        fields = ('nome_registro',)

class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = ('hora',)

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nome','horario')

class FrequenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Frequencia
        fields = ('tipo_registro','chefe','ipMaquina','dataHora','funcionario','consistente','inconsistente','justificativa')