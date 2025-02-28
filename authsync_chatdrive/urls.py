from django.contrib import admin
from django.urls import path, include
from .views import home  # Import the home view

urlpatterns = [
    path('', home, name='home'),  # Add this as the default route
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('chat/', include('chat.urls')),
    path('drive/', include('drive_app.urls')),
]
