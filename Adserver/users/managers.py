from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, if_brand,**extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, if_brand=False, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, if_brand=False, **extra_fields):
        return self._create_user(email, password, False, False, False
                                 **extra_fields)

    def create_superuser(self, email, password, if_brand=False, **extra_fields):
        return self._create_user(email, password, True, True, False
                                 **extra_fields)
