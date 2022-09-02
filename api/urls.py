from rest_framework.routers import SimpleRouter
from django.urls import path, include
from api.views.answer import AnswerView
from api.views.question import QuestionView
from api.views.questionAnswer import QuestionAnswerView
from api.views.user import UserView
from api.views.user_votes import UserVotes
from api.views.self_helps import SelfHelpViews

router = SimpleRouter()
router.register('answer', AnswerView, basename='answer')
router.register('question', QuestionView, basename='question')
router.register('user', UserView, basename='user')

urlpatterns = [
    path('questionanswer/<int:question_id>', QuestionAnswerView.as_view()),
    path('uservotes/<int:id>', UserVotes.as_view()),
    path('selfhelps', SelfHelpViews.as_view()),
    path('', include(router.urls)),
]