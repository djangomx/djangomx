import os
import sys
import site

site.addsitedir('/export/web/django.mx/virtualenv/lib/python2.7/site-packages')
BASE_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH_TWO = os.path.join(BASE_PATH)
sys.path.append('/export/web/django.mx/')
sys.path.append('/export/web/django.mx/djangomx/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
