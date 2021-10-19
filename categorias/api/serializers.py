from categorias.models import Materia, Banca
from rest_framework.serializers import ModelSerializer

class MateriaSerializer(ModelSerializer):    
    class Meta:
        model = Materia
        fields = ['materia',]


class BancaSerializer(ModelSerializer):    
    class Meta:
        model = Banca
        fields = ['banca']