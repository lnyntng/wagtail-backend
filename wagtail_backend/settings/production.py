from .base import *


DEBUG = False
TEMPLATE_DEBUG = False


try:
    from .local import *
except ImportError:
    pass


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8o4ts9rgsv55v',
        'USER': 'ggupiyudrbkhur',
        'PASSWORD': 'ggupiyudrbkhur',
        'HOST': 'ec2-54-83-51-0.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}