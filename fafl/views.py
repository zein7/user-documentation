import os
import json
import urllib
from shutil import copyfile, rmtree
import traceback
import mimetypes

import sphinx
from tempfile import mkdtemp


# import special tools for this platform
from .tools import Command, write_file

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

config_path = 'conf'


def build(timeout=10, build_dir=None, source_dir=None):
    # Replace this terrible implementation
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conf')
    source_path = source_dir #join('repos', 'source')
    build_path = build_dir #join('repos', 'build/html')
    command = ['sphinx-build', '-c', config_path, source_path, build_path]

    import subprocess

    p = subprocess.Popen(command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    p.wait()
    out, err = p.communicate()
    code = p.returncode

    return (code, out, err)

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
    if request.method == 'POST':
        rst = request.POST['code']
        write_file(branch_source_path, request.POST['code'])
        code, out, err = build(source_dir=branch_source_dir, build_dir=branch_html_dir)
        if code != 0:
            write_file(
                branch_build_path, 
                render_to_string('err.html', context={'err':err, 'out':out})
            )

    return render(request, 'edit.html', context={'filename':filename, 'rst':rst})

# @sphinxedit.route('/raw', methods = ['GET', 'POST'])
def raw(request, fn='index.html'):
    if not fn:
        fn='index.html'

    doc = open(os.path.join(base_dir, 'build', fn),'rb')

    content_type, encoding= mimetypes.guess_type(fn)

    return HttpResponse(doc, content_type=content_type)
