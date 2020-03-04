from .basesettings import *
import json
# Normally you should not import ANYTHING from Django directly into settings, but ImproperlyConfigured is an exception. 
from django.core.exceptions import ImproperlyConfigured


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

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['#######','##########', '#######', '###########']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # MySQL settings use the name of the db not the path
        'NAME': 'data_base_name_here',
        # Name of MySQL user on CPanel
        'USER': 'username_here',
        'PASSWORD': '##############',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Toggle block comment for local testing
''' ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # MySQL settings use the name of the db not the path
        'NAME': '##############',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '####',
    }
} '''
