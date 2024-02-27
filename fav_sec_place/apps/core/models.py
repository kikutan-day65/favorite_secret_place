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


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=128, unique=True, null=False)
    joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
