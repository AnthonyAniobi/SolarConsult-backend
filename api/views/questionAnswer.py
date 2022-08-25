from rest_framework.views import APIView
from rest_framework.response import Response
from consult.models.question_model import QuestionModel
from consult.models.answer_model import AnswerModel

class QuestionAnswerView(APIView):
    def get(self, response, question_id):
        question = QuestionModel.objects.get(id=int(question_id))
        answerModel = AnswerModel.objects.filter(question=question.id)
        answers = []
        for answer in answerModel:
            answers.append({
                'answer': answer.answer,
                'votes': answer.votes,
                'user': answer.user.id,
            })

        return Response({
            'id': question.id,
            'title': question.title,
            'question': question.question,
            'votes': question.votes,
            'user': question.user.id,
            'answers': answers,
        }) 