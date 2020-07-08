"""
Django settings for hololink project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'll_6@mme89*o#z##q7s_hh7g+wvs0f%8^_or_z*$c@nbi(#1!7'

# SECURITY WARNING: don't run with debug turned on in production!
from secret.hololink.settings import DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # This make it easier to integrate django templates with bootstrap things.
    'rest_framework',
    'widget_tweaks',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # For dynamic languages
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hololink.urls'

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

WSGI_APPLICATION = 'hololink.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

from secret.hololink.settings import (
    DATABASES,
)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

# We disable the most part of AUTH_PASSWORD_VALIDATORS for convinience of users.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# For i18n
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# This limits the set_language view option
LANGUAGES = {
    ('en', ''),
    ('zh-hant', ''),
}

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')

MEDIA_URL = '/uploads/'

# build-in auth system

#LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

# SMTP things
from secret.hololink.settings import (
    EMAIL_BACKEND,
    EMAIL_HOST,
    EMAIL_USE_TLS,
    EMAIL_PORT,
    EMAIL_HOST_USER,
    EMAIL_HOST_PASSWORD,
    DEFAULT_FROM_EMAIL,
    SERVER_EMAIL,
)
