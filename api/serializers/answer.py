from rest_framework import serializers

from consult.models.answer_model import AnswerModel

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = '__all__'