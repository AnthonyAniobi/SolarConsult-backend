from rest_framework.views import APIView
from rest_framework.response import Response
from consult.models.answer_model import AnswerModel
from consult.models.question_model import QuestionModel


class UserVotes(APIView):
    def get(self, response, id):
        user_id = int(id)
        question_votes = QuestionModel.objects.filter(user=user_id)
        answer_votes = AnswerModel.objects.filter(user=user_id)
        q_vote = 0
        for votes in question_votes:
            q_vote += votes.votes
        a_vote = 0
        for votes in answer_votes:
            a_vote += votes.votes
        return Response({
            'q-votes': q_vote,
            'a-votes': a_vote,
            # 'a-votes': answer_votes,
            'id':id
        })
