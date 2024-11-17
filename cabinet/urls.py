from django.template.defaulttags import url
from django.urls import path, include

from cabinet.views import UserRegistrationView, UserLoginAPIView, UserInfoRetrieveView, UserLogoutAPIView, \
    PasswordResetView, PasswordResetConfirmView, CustomUserUpdateView

urlpatterns = [
    path('register', UserRegistrationView.as_view()),
    path('login', UserLoginAPIView.as_view()),
    path('logout', UserLogoutAPIView.as_view()),
    path('me', UserInfoRetrieveView.as_view()),
    path('update/', CustomUserUpdateView.as_view()),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<int:uid>/<str:token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]