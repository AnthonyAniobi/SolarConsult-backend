from rest_framework import serializers

from consult.models.question_model import QuestionModel

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = '__all__'