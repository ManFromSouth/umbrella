from django.urls import path

from .views import RegisterRequest


urlpatterns = [
    path('signup/', RegisterRequest.as_view(), name='signup'),
]