from django.contrib.auth.models import User
from django.db import models

class QuestionModel(models.Model):
    title = models.CharField(max_length=250, verbose_name='question title')
    question = models.TextField(verbose_name='question text')
    votes = models.IntegerField(default=0, verbose_name='votes')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title