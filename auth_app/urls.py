from django.urls import path
from .views import GoogleLoginView

urlpatterns = [
    path('', GoogleLoginView.as_view(), name='google-login'),
]
