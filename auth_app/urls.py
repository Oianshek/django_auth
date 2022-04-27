from django.urls import path
from .views import *

urlpatterns = [
    path('auth/register/', RegisterApiView.as_view(), name='register'),
]
