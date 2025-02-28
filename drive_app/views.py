from rest_framework.views import APIView
from rest_framework.response import Response

class DriveAuthView(APIView):
    def get(self, request):
        return Response({"message": "Authenticate Google Drive"})

class UploadFileView(APIView):
    def post(self, request):
        return Response({"message": "Upload file to Google Drive"})
