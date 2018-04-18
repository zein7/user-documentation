import os
import sys

from aristotle_cloud.settings import *

sys.path.insert(1, BASE_DIR)

skip_migrations = os.environ.get(
    'ARISTOTLE_DEV_SKIP_MIGRATIONS',
    False
) is not False

if skip_migrations:  # pragma: no cover
    print("Skipping migrations")
    class DisableMigrations(object):
    
        def __contains__(self, item):
            return True
    
        def __getitem__(self, item):
            return None
    
    MIGRATION_MODULES = DisableMigrations()


INSTALLED_APPS = (
    # The good stuff
    'docs_server',
) + INSTALLED_APPS
ARISTOTLE_SETTINGS_LOADER = "aristotle_cloud.utils.yaml_settings_loader.settings_loader"


# https://docs.djangoproject.com/en/1.10/topics/testing/overview/#speeding-up-the-tests
# We do a lot of user log in testing, this should speed stuff up.
PASSWORD_HASHERS = (
    'docs_server.insecure.DoubleROT13PasswordHasher',
)

# ARISTOTLE_SETTINGS['BULK_ACTIONS'] = ARISTOTLE_SETTINGS['BULK_ACTIONS']+[
#     'aristotle_mdr.forms.bulk_actions.QuickPDFDownloadForm',
#     'aristotle_mdr.contrib.slots.forms.BulkAssignSlotsForm',
# ]

ROOT_URLCONF = 'docs_server.urls'

ARISTOTLE_SETTINGS['CONTENT_EXTENSIONS'] = ARISTOTLE_SETTINGS['CONTENT_EXTENSIONS'] + ['aristotle_mdr_links']
ARISTOTLE_SETTINGS['SITE_NAME'] = "My Registry"
ARISTOTLE_SETTINGS['SITE_INTRO'] = "Use Aristotle Metadata Registry to search for metadata..."
# ARISTOTLE_SETTINGS['SITE_BRAND'] =  '/aristotle_mdr/images/aristotle_small.png'

MIDDLEWARE = [
    'aristotle_cloud.middleware.AllAllowedHostsHealthCheckerMiddleware',
    # This screws us up
    # 'aristotle_cloud.middleware.URLReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'aristotle_mdr.contrib.redirect.middleware.RedirectMiddleware',
    'django_limits.middleware.LimitExceededMiddleware',
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
]


SECURE_SSL_REDIRECT = False
