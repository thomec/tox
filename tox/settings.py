# tox/settings.py


"""
Django settings for tox project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""


import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4suxcw2cz@o6lx*t1i88zik!h&(b3)(vg#)s%1yqw-ayv=(0qw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# needed if not DEBUG
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'beule']


# Applications and middelware settings
# set urls.py

INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'registration', # django-registration-redux
        'rango',
        'polls',
        'crispy_forms',
        'mathapp',
        'pollit',
        'pollngo',
        )

MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        )

ROOT_URLCONF = 'tox.urls'


# Template engine
# added from tango to use in TEMPLATES

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
        {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH,],
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

WSGI_APPLICATION = 'tox.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
        'default': {
                # 'ENGINE': 'django.backends.mysql', # 'django.db.backends.sqlite3',
                # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'tox',
                'USER': 'tox',
                'PASSWORD': 'toxuser',
                'HOST': '127.0.0.1',
                'PORT': '3306'
                },
        }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


# added from tango
# static and media files

STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
        STATIC_PATH,
        )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# registration
# django-registration-redux

REGISTRATION_OPEN = True        # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/rango/'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'  # The page users are directed to if they are not logged in,
                                # and are trying to access pages requiring authentication

# settings for
# Crispy-Forms

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG


# additional information
# print environment vars on screen

if DEBUG:
    print("reading settings from:\n\t"+os.path.abspath(__file__))

    print("BASE_DIR      = "+str(BASE_DIR))
    print("TEMPLATE_DIRS = "+str(TEMPLATES[0]['DIRS']))
    print("STATIC_PATH   = "+str(STATIC_PATH))
    print("MEDIA_ROOT    = "+str(MEDIA_ROOT))
    print("MEDIA_URL     = "+str(MEDIA_URL))
    print("\n\n")


