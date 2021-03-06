#!/usr/bin/env python
# This file should not ever need editing
"""Django's command-line utility for administrative tasks."""
import os
import sys

# If you change your project hierarchy or settings files names, update the path to settings file here
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.productionsettings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
