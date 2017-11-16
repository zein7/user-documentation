#-*- coding: utf-8 -*-
"""
Django settings for possum_mdr project.

"""
from decouple import config

from server.settings import *
from aristotle_cloud.settings import *
from aristotle_cloud.env.twelve_factor_settings import *


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
) + INSTALLED_APPS

