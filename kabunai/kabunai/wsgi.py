"""
WSGI config for kabunai project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import django.core.handlers.wsgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kabunai.settings')

application = django.core.handlers.wsgi.WSGIHandler()
# application = get_wsgi_application()
