from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number=None, name=None, password=None, is_admin=False, is_staff=False,
                    is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.phone_number = phone_number
        user.set_password(password)
        user.name = name
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number=None, name=None, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.phone_number = phone_number
        user.set_password(password)
        user.name = name
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user