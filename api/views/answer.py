from rest_framework import viewsets
from consult.models.answer_model import AnswerModel
from api.permissions.isAuthorOrReadOnly import IsAuthorOrReadOnly
from api.serializers.answer import AnswerSerializer

class AnswerView(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer