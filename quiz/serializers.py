from rest_framework import serializers;
from .models import Question, Form


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ["created_at","updated_at"]



class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        exclude = ["created_at","updated_at", "creator", "id"]


    def to_representation(self, instance):
        questions = []
        for question in instance.questions.all():
            choices = None
            if question.question_type in ["multiple choices","checkbox"]:
                choices = []
                for choice in question.question_choice.all():
                    choices.append(choice.choice)

            questions.append({
                "question": instance.question,
                "question_type": instance.question_type,
                "required": instance.required,
            })


        return super().to_representation(instance)