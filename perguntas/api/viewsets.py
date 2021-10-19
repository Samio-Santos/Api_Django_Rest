from perguntas.api.serializers import CespeSerializer, VunespSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from perguntas.models import Pergunta


class CespeViewSet(ModelViewSet):
    serializer_class = CespeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Pergunta.objects.filter(banca__banca="Cespe", disponivel=True)


class VunespViewSet(ModelViewSet):
    queryset = Pergunta.objects.filter(banca__banca="Vunesp", disponivel=True)
    serializer_class = VunespSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
