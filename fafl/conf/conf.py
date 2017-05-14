import os, sys
user_doc_path = os.path.abspath('../../')
sys.path.insert(0, user_doc_path)

from docs.conf import *

screenshots_server_path = 'http://0.0.0.0:8080'
screenshots_read_path = '/_static/screenshots'
# screenshots_save_path = os.path.abspath(os.path.join('/tmp/fafl/build',screenshots_read_path[1:]))
screenshots_save_path = os.path.abspath(os.path.join('.',screenshots_read_path[1:]))
html_theme_path = [os.path.join(user_doc_path, 'docs', '_themes')]

import solar_theme

html_theme = 'aristotle_theme'
