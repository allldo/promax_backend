from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if "@" in username:
            filter_args = {'email': username}
        else:
            filter_args = {'phone_number': username}

        try:
            user = CustomUser.objects.get(**filter_args)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
