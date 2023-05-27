"""
Django settings for studentstudyportal project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_ROOT=os.path.dirname(os.path.abspath(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bku)a)g%0l^0^fv2x&wjcu#m_6*6z8&=8$2xz75)v1_i4h1dj8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False



ALLOWED_HOSTS = ['codeblazestudyapp.herokuapp.com','localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
    'crispy_forms',
    'custom_user'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'studentstudyportal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'dashboard/templates'],
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

WSGI_APPLICATION = 'studentstudyportal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse("postgres://kc:qQt31MNsC8BLwXVRV82SSJ0LFDVmh6ii@dpg-chokebik728ivvtld5m0-a.oregon-postgres.render.com/codeblazestudyappdb")
    }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME':'d2m1bcvhpji35l',
#         'USER':'qccunzwbaqsneu',
#         'PASSWORD':'04e52f7ef263438e3bf16f9e1f7d0aaa3815d88da154ff521ef1769d8eb69234',
#         'HOST':'ec2-34-234-240-121.compute-1.amazonaws.com',
#         'PORT':'5432'
#     }
    
# }

# DATABASES = {
#  'default': {
#  'ENGINE': 'django.db.backends.sqlite3',
#  'NAME': BASE_DIR / 'db.sqlite3',
#  }
# }




# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
CRISPY_TEMPLATE_PACK="bootstrap4"
LOGIN_REDIRECT_URL='index'
LOGIN_URL='login'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


