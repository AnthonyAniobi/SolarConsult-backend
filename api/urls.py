from rest_framework.routers import SimpleRouter
from django.urls import path, include
from api.views.answer import AnswerView
from api.views.question import QuestionView
from api.views.questionAnswer import QuestionAnswerView

router = SimpleRouter()
router.register('answer', AnswerView, basename='answer')
router.register('question', QuestionView, basename='question')

urlpatterns = [
    path('questionanswer/<int:question_id>', QuestionAnswerView.as_view() ),
    path('', include(router.urls)),
]