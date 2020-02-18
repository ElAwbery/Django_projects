"""
WSGI config for charlieawbery (config module) project.
WSGI works by defining a callable object (a function as variable) called 
'application' inside this WSGI file. This callable expects a request object, 
which the WSGI server provides; and returns a response object, which the 
WSGI server serializes and sends to the client.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
