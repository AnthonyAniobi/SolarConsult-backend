from django.contrib.auth.models import User
from django.db import models

from consult.models.question_model import QuestionModel

class AnswerModel(models.Model):
    answer = models.TextField(verbose_name='answer text')
    votes = models.IntegerField(default=0, verbose_name='votes')
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.answer[:5]