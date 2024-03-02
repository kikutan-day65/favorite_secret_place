from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings

from uuid import uuid4


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=64)


class CustomUserModel(BaseUserManager):
    def create_user(self, username, email, password):
        if not email:
            raise ValueError("Users must have an email address")
        new_user = self.model(username=username, email=self.normalize_email(email))
        new_user.set_password(password)
        new_user.save()
        return new_user
    
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=128, unique=True)
    joined = models.DateField(auto_now_add=True)

    objects = CustomUserModel()

    def __str__(self):
        return self.username


class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='places')
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='places'
    )

    def __str__(self):
        return self.name


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    photo_path = models.CharField(max_length=255, unique=True)
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

    def __str__(self):
        return self.photo_path


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    body = models.TextField()
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

    def __str__(self):
        return self.body


class Like(models.Model):
    value = models.BooleanField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        unique_together = ('user', 'place')
