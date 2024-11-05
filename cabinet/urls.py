from django.urls import path

from cabinet.views import UserRegistrationView, UserLoginAPIView, UserInfoRetrieveView, UserLogoutAPIView

urlpatterns = [
    path('register', UserRegistrationView.as_view()),
    path('login', UserLoginAPIView.as_view()),
    path('logout', UserLogoutAPIView.as_view()),
    path('me', UserInfoRetrieveView.as_view()),
]