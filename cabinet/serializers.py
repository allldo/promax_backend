from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField, ImageField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, Serializer

from .models import CustomUser

class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)
    avatar = ImageField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'phone_number', 'name', 'avatar')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class CustomUserUpdateSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone_number', 'avatar']

    def validate_email(self, value):
        user = self.instance
        if CustomUser.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise ValidationError("Этот email уже используется.")
        return value


class UserLoginSerializer(ModelSerializer):
    id = PrimaryKeyRelatedField(read_only=True)
    username = CharField()
    password = CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "password"]

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if not CustomUser.objects.filter(email=username).exists() and not CustomUser.objects.filter(phone_number=username).exists():
            raise ValidationError({"email": "User does not exist!"})

        user = authenticate(request=self.context.get('request'), username=username, password=password)

        if not user:
            raise ValidationError({"password": "Incorrect password!"})

        data['user'] = user
        return data


class PasswordResetSerializer(Serializer):
    email = EmailField()

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise ValidationError("Пользователь с этим email не найден.")
        return value


class PasswordResetConfirmSerializer(Serializer):
    new_password = CharField(write_only=True)
    confirm_password = CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise ValidationError("Пароли не совпадают.")
        return data

    def save(self, user):
        user.set_password(self.validated_data['new_password'])
        user.save()