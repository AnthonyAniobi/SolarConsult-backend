from rest_framework import viewsets
from consult.models.question_model import QuestionModel
from api.permissions.isAuthorOrReadOnly import IsAuthorOrReadOnly
from api.serializers.question import QuestionSerializer

class QuestionView(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer