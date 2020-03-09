"""
Django settings for charlieawbery projects.
This is a dummy file. 

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Don't hardcode paths to variables in settings. See "handling file paths 
# in settings" in Two Scoops.
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import json
# Normally you should not import ANYTHING from Django directly into settings, but ImproperlyConfigured is an exception. 
from django.core.exceptions import ImproperlyConfigured

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['server IP and port here']


# Gets secret key from secrets module
with open('charlieawbery_root/secrets.json') as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exception'''
    try: 
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment.variable'.format(setting)
        raise ImproperlyConfigured(error_msg)
        
SECRET_KEY = get_secret('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Additional apps
    'hubapp.apps.HubappConfig',
    'charlieawbery_root.apps.Charlieawbery_rootConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# Don't hardcode paths to templates. See "handling file paths in settings" 
# in Two Scoops.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # MySQL settings use the name of the db not the path
        'NAME': '####################',
        # Name of MySQL user on CPanel is doubled. e.g. if name is djangobrian, username would be djangobrian_djangobrian
        'USER': '#####################',
        'PASSWORD': '#################',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'



