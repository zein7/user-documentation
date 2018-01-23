import os
import sys
import json
import urllib
from shutil import copyfile, rmtree
import traceback
import mimetypes

import sphinx
from tempfile import mkdtemp
from io import StringIO

# import special tools for this platform
from .tools import Command, write_file

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

config_path = 'conf'

class RedirectStdStreams(object):
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr



def build(timeout=10, build_dir=None, source_dir=None):
    from sphinx.application import Sphinx
    from sphinx.cmdline import handle_exception
    import optparse
    
    srcdir = source_dir
    confdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conf')
    outdir = build_dir
    doctreedir = os.path.abspath(os.path.join(outdir, '.doctrees'))
    builder = 'html'
    out = StringIO()
    err = StringIO()
    opts, args = optparse.OptionParser().parse_args([])
    with RedirectStdStreams(stdout=out, stderr=err):
    #     None
    # if True:
        app = Sphinx(srcdir, confdir, outdir, doctreedir, builder,
            #confoverrides, status, warning, args.freshenv,
            # args.warningiserror, args.tags, args.verbosity, args.jobs
        )
        try:
            app.build() #args.force_all, filenames)
            return (app.statuscode, out.getvalue(), err.getvalue())
        except Exception as e:
            err_text = handle_exception(app, opts, e, stderr=err)
            return (-1, out.getvalue(), err.getvalue())

filename = 'index'
base_dir = '/tmp/fafl/'


def mk_if_not_exists(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def edit(request):
    tmpdir = "/tmp/fafl" #mkdtemp(prefix="fafl-build-")
    mk_if_not_exists(tmpdir)

    branch_source_dir = os.path.join(tmpdir,'source')
    mk_if_not_exists(branch_source_dir)

    branch_html_dir = os.path.join(tmpdir,'build')
    mk_if_not_exists(branch_html_dir)
    
    branch_source_path = os.path.join(branch_source_dir, 'index.rst')
    branch_build_path = os.path.join(branch_html_dir, 'index.html')

    rst=""
    err=""
    out=""
    if request.method == 'POST':
        rst = request.POST['code']
        write_file(branch_source_path, request.POST['code'])
        code, out, err = build(source_dir=branch_source_dir, build_dir=branch_html_dir)
        if code != 0:
            write_file(
                branch_build_path, 
                render_to_string('fafl/err.html', context={'err':err, 'out':out})
            )

    return render(request, 'fafl/edit.html', context={'filename':filename, 'rst':rst, "err": err, "out": out})


# @sphinxedit.route('/raw', methods = ['GET', 'POST'])
def raw(request, fn='index.html'):
    if not fn:
        fn='index.html'

    doc = open(os.path.join(base_dir, 'build', fn),'rb')

    content_type, encoding= mimetypes.guess_type(fn)

    return HttpResponse(doc, content_type=content_type)


def home(request):
    return render(request, 'fafl/home.html', context={})


def help(request):
    return render(request, 'fafl/help.html', context={})


from django.core.management import call_command
from io import StringIO
import yaml

def dumper(request):
    dump = ""
    if request.POST:
        out = StringIO()

        call_command(
            'dumpdata', format="yaml",
            exclude=[
                'auth', 'contenttypes', 'aristotle_mdr_help',
                'easyaudit', # Not sure I want this yet
                'notifications', 'sessions',
            ],
            use_natural_foreign_keys=True,
            stdout=out
        )
        dump = out.getvalue()
        dump = [
            x for x in yaml.load(dump)
            if x['model'] not in [
                # our exceptional objects which cause problems...
                'aristotle_mdr.possumprofile',
            ]  
        ]
        dump = str(yaml.dump(dump))
        
    return render(
        request, 'fafl/dumper.html',
        context={"dump":dump}
    )


def loader(request):
    import tempfile
    
    dump = ""
    data = ""
    dumps = []
    if request.POST:
        data = request.POST['data']
        f = tempfile.NamedTemporaryFile('w', delete=False, suffix=".yaml")
        f.write(data)
        f.close()

        out = StringIO()

        try:
            call_command(
                'loaddata', f.name, format="yaml",
                stdout=out
            )
            dump = out.getvalue ()
            dumps.append(dump)
        except Exception as e:
            dumps.append(e)

    dumps = "\n\n".join([str(s) for s in dumps])
    return render(
        request, 'fafl/loader.html',
        context={"dump":dumps, "data":data}
    )


def resetter(request):
    import tempfile
    
    dump = ""
    data = ""
    dumps = []
    if request.POST:
        out = StringIO()

        try:
            call_command(
                'flush', interactive=False,
                stdout=out
            )
            # from django.contrib.contenttypes.models import ContentType
            # content_types = ContentType.objects.all()
            # print("\n".join([
            #     str([ct.pk, ct]) for ct in content_types
            # ]))
            dump += out.getvalue ()

            call_command(
                'migrate',  interactive=False,
                stdout=out
            )
            dump += out.getvalue ()
            call_command(
                'loaddata', 'server/fixtures/users.yaml', format="yaml",
                stdout=out
            )
            dump += out.getvalue ()
            call_command(
                'loaddata', 'server/fixtures/iso_metadata.json', format="json",
                stdout=out
            )
            dump += out.getvalue ()
            call_command(
                'loaddata', 'server/fixtures/test_metadata.yaml', format="yaml",
                stdout=out
            )
            call_command(
                'load_aristotle_help',
                stdout=out
            )
            dump += out.getvalue ()
            call_command(
                'rebuild_index', noinput=False,
                stdout=out
            )
            dump += out.getvalue ()
            dumps.append(dump)
        except Exception as e:
            dumps.append(e)


    dumps = "\n\n".join([str(s) for s in dumps])
    return render(
        request, 'fafl/resetter.html',
        context={"dump":dumps, "data":data}
    )
