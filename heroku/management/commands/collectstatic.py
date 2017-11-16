import os
import subprocess

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from django.test import override_settings
import static_precompiler

class Command(BaseCommand):
    args = ''
    help = 'Compiles and Collects all staticfiles into the static path'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--noinput",
            default=False,
            action='store_true',
        )

    def handle(self, *args, **options):

        if "static_precompiler" in settings.INSTALLED_APPS:
            call_command('compile_and_collect')
        else:
            call_command('base_collectstatic', '--noinput', verbosity=3)

