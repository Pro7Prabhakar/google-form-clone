from django.urls import path, include
from quiz.views import QuestionAPI, FormAPI

urlpatterns = [
    path('questions/', QuestionAPI.as_view()),
    path('form/<pk>/', FormAPI.as_view())
]
