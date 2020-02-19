import sys, os

# Passenger on cPanel runs the default python, which is python 2
# So the first thing we do is force a switch to the python3 in our
# virtualenv
INTERP = "/home/charlie/charlieawbery/env/bin/python3"

# Check to see whether we're running the correct python. The first 
# time this runs, we won't be! Second time round, we should be.
# sys.executable is the path of the running python.
#
# First argument to execl is the program to execute (INTERP); the 
# second argument is the first part of the arguments to it, which
# is the full path to the executable itself. sys.argv is the rest
# of the argumnets originally passed to us.
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

environ=os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.productionsettings')

# This is the information Passenger needs to talk to python via WSGI.
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

# This is the recommended code for the file from Django
from wsgi import app
application = app
