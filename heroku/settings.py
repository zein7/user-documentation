#-*- coding: utf-8 -*-
"""
Django settings for possum_mdr project.

"""
from decouple import config

from server.settings import *
from aristotle_cloud.settings import *
from aristotle_cloud.env.twelve_factor_settings import *

ARISTOTLE_CLOUD_PLAN = 'large'


MIDDLEWARE_CLASSES = (
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

HAYSTACK_SIGNAL_PROCESSOR = 'aristotle_mdr.contrib.help.signals.AristotleHelpSignalProcessor'

INSTALLED_APPS = (
    'heroku',
    'fafl',
    'aristotle_mdr.contrib.self_publish',
    'server',
) + INSTALLED_APPS

ROOT_URLCONF = 'heroku.urls'

ARISTOTLE_SETTINGS['CONTENT_EXTENSIONS'] = ARISTOTLE_SETTINGS['CONTENT_EXTENSIONS'] + ['aristotle_mdr_links']
ARISTOTLE_SETTINGS['SITE_NAME'] = "My Registry"
ARISTOTLE_SETTINGS['SITE_INTRO'] = "Use Aristotle Metadata Registry to search for metadata..."
ARISTOTLE_SETTINGS['SITE_BRAND'] =  'aristotle_mdr/images/aristotle_small.png'


ARISTOTLE_SETTINGS['BULK_ACTIONS'] = ARISTOTLE_SETTINGS['BULK_ACTIONS']+[
    'aristotle_mdr.forms.bulk_actions.QuickPDFDownloadForm',
    'aristotle_mdr.contrib.slots.forms.BulkAssignSlotsForm',
]
