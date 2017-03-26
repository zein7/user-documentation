import os
import subprocess
from tempfile import mkdtemp

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from django.test import override_settings
import static_precompiler

class Command(BaseCommand):
    args = '<workgroup_id workgroup_id ...>'
    help = 'Compiles all staticfiles into '

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        # parser.add_argument('-O',
        #     "--output_path",
        #     metavar="output_path",
        #     default=False,
        #     help="Path to the Django file storage object (e.g. django.core.files.storage.default_storage).",
        # )
        parser.add_argument(
            "--noinput",
            default=False,
            action='store_true',
        )

    def handle(self, *args, **options):
        compile_dir = options.get('output_path', mkdtemp())
        print(compile_dir)

        with override_settings(
            # STATIC_ROOT = compile_dir,
            # OUTPUT_DIR = compile_dir,
            # DEBUG = False,  # We need this off for manifest to work
            # # STATIC_PRECOMPILER_ROOT = compile_dir,
            # # STATICFILES_DIRS = tuple(
            # #     list(settings.STATICFILES_DIRS) + [compile_dir]
            # # ),
            # STATICFILES_FINDERS = (
            #     'django.contrib.staticfiles.finders.FileSystemFinder',
            #     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
            #     'static_precompiler.finders.StaticPrecompilerFinder',
            # ),
            # STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage',
        ):
            # static_precompiler.settings.STATIC_ROOT = compile_dir
            # static_precompiler.settings.ROOT = compile_dir
            # print('Preparing to compile')
            call_command('compilestatic')
            # num_files = sum([len(files) for r, d, files in os.walk(compile_dir)])
            # print('Compiled - %s files' % num_files)
            call_command('base_collectstatic', '--noinput', verbosity=3)

        print('All done!')

