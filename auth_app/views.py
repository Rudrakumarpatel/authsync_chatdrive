from rest_framework.response import Response
from rest_framework.views import APIView
from social_django.utils import psa

class GoogleLoginView(APIView):
    def get(self, request):
        return Response({"message": "Redirect to Google OAuth for authentication"})
