from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from cabinet.models import CustomUser
from cabinet.serializers import UserSerializer, UserLoginSerializer, PasswordResetSerializer, \
    PasswordResetConfirmSerializer, CustomUserUpdateSerializer
from orders.models import ProductOrder
from orders.serializers import OrderSerializer


class UserRegistrationView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            response = {
                "email": {
                    "detail": "User Doesnot exist!"
                }
            }
            if CustomUser.objects.filter(email=request.data['username']).exists() or CustomUser.objects.filter(phone_number=request.data['username']).exists():
                try:
                    user = CustomUser.objects.get(email=request.data['username'])
                except CustomUser.DoesNotExist:
                    user = CustomUser.objects.get(phone_number=request.data['username'])
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    'success': True,
                    'email': user.email,
                    'phone_number': user.phone_number,
                    'token': token.key
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        send_mail(
            subject="wqe", message="qwe", from_email="dotan2.maks@mail.ru", recipient_list=["dotan2.maks@mail.ru"]
        )
        return Response(status=status.HTTP_200_OK, data={"logged out": True})

class UserInfoRetrieveView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes  = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class CustomUserUpdateView(UpdateAPIView):
    serializer_class = CustomUserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

token_generator = PasswordResetTokenGenerator()

class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = CustomUser.objects.get(email=email)
            token = token_generator.make_token(user)
            reset_url = f"http://188.225.18.241:3001/?password-reset-confirm=true&id={user.id}&key={token}/"

            # Отправка письма
            send_mail(
                'Восстановление пароля',
                f'Перейдите по ссылке для смены пароля: {reset_url}',
                'dotan2.maks@mail.ru',
                [email],
                fail_silently=False,
            )

            return Response({"detail": "Ссылка для восстановления пароля отправлена на почту."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    def post(self, request, uid, token):
        user = CustomUser.objects.get(pk=uid)
        if not token_generator.check_token(user, token):
            return Response({"detail": "Неверный или истекший токен."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({"detail": "Пароль успешно изменен."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOrderListView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return ProductOrder.objects.filter(user=self.request.user).prefetch_related('order_items__product')
