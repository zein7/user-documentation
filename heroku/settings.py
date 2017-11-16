#-*- coding: utf-8 -*-
"""
Django settings for possum_mdr project.

"""
from server.settings import *

BASE_DIR = os.environ.get(
    'aristotlemdr__BASE_DIR',
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'site')
)

STATIC_PRECOMPILER_COMPILERS = (
    ('static_precompiler.compilers.LESS', {"executable": "lesscpy"}),
)

import os

from server.settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'site')
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
FIXTURES_DIRS = [os.path.join(BASE_DIR, 'fixtures')]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
# This is a sub-directory under the MEDIA_ROOT where uploads from CKEDITOR are placed.
CKEDITOR_UPLOAD_PATH = 'uploads/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'aristotle_mdr.contrib.redirect.middleware.RedirectMiddleware',
)

WSGI_APPLICATION = 'heroku.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#Aristotle settings are below, settings these gives the ability to personalise this particular installation.

from urllib.parse import urlparse
es = (
    os.environ.get('SEARCHBOX_URL', None) or
    os.environ.get('BONSAI_URL', None)
)

if es is not None:
    es = urlparse(es)
    port = es.port or 80
    
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack_elasticsearch.elasticsearch5.Elasticsearch5SearchEngine',
            'URL': es.scheme + '://' + es.hostname + ':' + str(port),
            'INDEX_NAME': 'documents',
        },
    }
    if es.username:
        HAYSTACK_CONNECTIONS['default']['KWARGS'] = {"http_auth": es.username + ':' + es.password}
else:
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'aristotle_mdr.contrib.search_backends.facetted_whoosh.FixedWhooshEngine',
            'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
            'INCLUDE_SPELLING': True,
        },
    }
HAYSTACK_SIGNAL_PROCESSOR = 'aristotle_mdr.contrib.help.signals.AristotleHelpSignalProcessor'

INSTALLED_APPS = (
    'heroku',
) + INSTALLED_APPS



DEBUG = os.environ.get('aristotlemdr__DEBUG', False) == 'True'
print('Debug is', DEBUG)
ALLOWED_HOSTS = os.environ.get('aristotlemdr__ALLOWED_HOSTS').split(',')


LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console-simple': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'aristotle_mdr': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

