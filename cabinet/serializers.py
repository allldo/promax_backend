from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from .models import CustomUser

class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'phone_number')


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
        if not CustomUser.objects.filter(username=username).exists():
            raise ValidationError({"username": "User does not exist!"})

        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError({"password": "Incorrect password!"})

        data['user'] = user
        return data