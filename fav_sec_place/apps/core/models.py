from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings

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


class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=128, null=False)
    address = models.CharField(max_length=255, null=False)
    description = models.TextField()
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='places'
    )

    def __str__(self):
        return self.name


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    photo_path = models.CharField(max_length=255, unique=True, null=False)
    place_id = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='photos'
    )


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    body = models.TextField(null=False)
    posted = models.DateTimeField(auto_now_add=True)
    place_id = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
