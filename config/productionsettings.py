from .basesettings import *

DEBUG = False

ALLOWED_HOSTS = ['67.20.55.28', 'charlieawbery.com', 'luckyegg.org', 'idletwilight.com', 'meaningness.com',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # MySQL settings use the name of the db not the path
        'NAME': 'charlieawbery',
        # Name of MySQL user on CPanel is 'charlie'
        'USER': 'charlie_charlie',
        'PASSWORD': 'LbDT3ryu9uug',
        'HOST': 'localhost',
        'PORT': '',
    }
}
