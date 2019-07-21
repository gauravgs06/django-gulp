from .base import *

DEBUG = TEMPLATE_DEBUG = False

ROOT_URLCONF = '{{ project_name }}.urls.prod_urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

INSTALLED_APPS += [

]

