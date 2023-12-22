from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, UserManager

from django.db import models


class UserManager(UserManager):
    def create_user(self, email, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=email)
        user.set_password(password)
        user.save(using=self.db)

        return user


class User(AbstractBaseUser):
    USERNAME_FIELD = "email"
    username = None
    REQUIRED_FIELDS = []

    objects = UserManager()
