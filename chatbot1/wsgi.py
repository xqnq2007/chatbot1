"""
WSGI config for chatbot1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/Users/css/djangoprojects/chatbot1')
sys.path.append('/Users/css/djangoprojects/chatbot1/chatbot1')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatbot1.settings")
#os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'
application = get_wsgi_application()
