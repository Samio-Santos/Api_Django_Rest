from perguntas.models import Pergunta
from rest_framework.serializers import ModelSerializer
from categorias.api.serializers import MateriaSerializer, BancaSerializer

class CespeSerializer(ModelSerializer):
    materia = MateriaSerializer(read_only=True)
    banca = BancaSerializer(read_only=True)

    class Meta:
        model = Pergunta
        fields = ['id', 'texto', 'enunciado', 'alternativas_correta', 'materia', 'banca', 'disponivel']


class VunespSerializer(ModelSerializer):
    materia = MateriaSerializer(read_only=True)
    banca = BancaSerializer(read_only=True)

    class Meta:
        model = Pergunta
        fields = ['id', 'texto', 'enunciado', 'alternativas_Multiplasescolhas', 'alternativas_correta', 'materia', 'banca', 'disponivel']