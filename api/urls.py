from django.urls import path, include
from quiz.views import QuestionAPI

urlpatterns = [
    path('questions/', QuestionAPI.as_view())
]
