from django.contrib import admin
from consult.models.answer_model import AnswerModel

from consult.models.question_model import QuestionModel

# Register your models here.
admin.site.register([
    QuestionModel,
    AnswerModel,
])