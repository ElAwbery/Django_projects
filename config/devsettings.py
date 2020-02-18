from .basesettings import *

# Order of variables matters. SECRET_KEY must come first. 
SECRET_KEY = '_hs65QtB2tbXToswjL_0w1SqjO4ggzIHzA'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # MySQL settings use the name of the db not the path
        'NAME': 'charlieawbery',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '8889',
    }
}

