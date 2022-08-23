from rest_framework.routers import SimpleRouter
from django.urls import path, include
from api.views.answer import AnswerView
from api.views.question import QuestionView

router = SimpleRouter()
router.register('answer', AnswerView, basename='answer')
router.register('question', QuestionView, basename='question')

urlpatterns = [
    # path('', )
    path('', include(router.urls))
]