from django.urls import path

from .views import register_request


urlpatterns = [
    path('signup/', register_request.as_view(), name='signup'),
]