"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 강의에서는 BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 으로 사용
BASE_DIR = Path(__file__).resolve().parent.parent
# print("------")
# print(os.path.join(BASE_DIR, "uploads"))
# print("------")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*1fr(^a$tupj@s9h^f8f^7hrs4kj5054o0ee6#h*818&t8*$oo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# bool(os.environ.get("DEBUG"))

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

PROJECT_APPS = [
    'core.apps.CoreConfig', 'users.apps.UsersConfig', 'rooms.apps.RoomsConfig',
    'reviews.apps.ReviewsConfig', 'reservations.apps.ReservationsConfig',
    'lists.apps.ListsConfig', 'conversations.apps.ConversationsConfig'
]

THIRD_PARTY_APPS = ['django_countries', 'django_seed']

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config/wsgi:application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if DEBUG is False:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': os.environ.get("RDS_HOST"),
            'NAME': os.environ.get("RDS_NAME"),
            'USER': os.environ.get("RDS_USER"),
            "PASSWORD": os.environ.get("RDS_PASSWORD"),
            "PORT": "5432",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


AUTH_USER_MODEL = 'users.User'


MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")

MEDIA_URL = "/media/"
# MEDIA_URL은 MEDIA_ROOT로 부터 얻어지는 media를 다룬다. 여기서는 그 이름을 media로 정한거고, 그 명칭은 /(slash)로 끝나야 한다.
# media 앞에 / 쓴것은 절대경로로 바꾸기 위해서 root를 넣은 것 - 이를 안넣어주면 url이 상대경로로 표현됨


# Email Configuration

EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = '587'
EMAIL_HOST_USER = os.environ.get('MAILGUN_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_PASSWORD')
EMAIL_FROM = 'sexy-guy@sandboxb1cf09eea119459397e648dea47ee582.mailgun.org'


# Auth

LOGIN_URL = "users/login/"


# Locale
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)
