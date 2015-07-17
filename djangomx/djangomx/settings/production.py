from common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = SECRETS.get('email_host', '')
