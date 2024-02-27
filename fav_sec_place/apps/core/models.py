from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from uuid import uuid4


class CustomUserModel(BaseUserManager):
    def create_user(self, username, email, password):
        if not email:
            raise ValueError("Users must have an email address")
        new_user = self.model(username=username, email=self.normalize_email(email))
        new_user.set_password(password)
        new_user.save()
        return new_user
