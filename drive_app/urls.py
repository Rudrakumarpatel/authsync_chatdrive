from django.urls import path
from .views import DriveAuthView, UploadFileView

urlpatterns = [
    path('connect/', DriveAuthView.as_view(), name='drive-connect'),
    path('upload/', UploadFileView.as_view(), name='file-upload'),
]
