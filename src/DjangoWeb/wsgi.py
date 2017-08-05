#coding=utf-8 
"""
WSGI config for DjangoWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

print sys.path
sys.path.append('/Library/Python/2.7/site-packages/psycopg2-2.7.1-py2.7-macosx-10.11-intel.egg')
sys.path.append('/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg')
sys.path.append('/Library/Python/2.7/site-packages')  
print sys.path

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoWeb.settings")

application = get_wsgi_application()
