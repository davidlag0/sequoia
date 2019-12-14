#!/usr/bin/env python
"""Django Management"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sequoia.settings")
    try:
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Code coverage is handled here because of a bug with Django and nose that
    # hasn't been fixed after years.
    IS_TESTING = 'test' in sys.argv

    if IS_TESTING:
        from coverage import Coverage
        COV = Coverage()
        COV.erase()
        COV.start()

    execute_from_command_line(sys.argv)

    if IS_TESTING:
        COV.stop()
        COV.save()
        COV.report()
        COV.html_report(directory='htmlcov')
