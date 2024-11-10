from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from .models import CustomUser

class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'phone_number')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserLoginSerializer(ModelSerializer):
    id = PrimaryKeyRelatedField(read_only=True)
    email = EmailField()
    password = CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password"]

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if not CustomUser.objects.filter(email=email).exists():
            raise ValidationError({"email": "User does not exist!"})
        print(email)
        user = authenticate(request=self.context.get('request'), email=email, password=password)
        if not user:
            raise ValidationError({"password": "Incorrect password!"})

        data['user'] = user
        return data