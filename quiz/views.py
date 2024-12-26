from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question




class QuestionAPI(APIView):

    def get(self):
        
        return Response({
            "status": True,
            "message": "questions fetched successfully",
            "data": {}
        })