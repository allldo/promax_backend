from django.urls import path

from cabinet.views import UserRegistrationView, UserLoginAPIView

urlpatterns = [
    path('register', UserRegistrationView.as_view()),
    path('login', UserLoginAPIView.as_view()),
]