"""
python manage.py runserver 0.0.0.0:8000 --settings=config.settings.develop
で設定ファイル読み込んで起動
"""
from .base import *
from decouple import config


SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fav_sec_place',
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5432
    }
}
