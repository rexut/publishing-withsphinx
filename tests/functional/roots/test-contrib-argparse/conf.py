# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('../../samples'))

needs_sphinx = '1.3'
# FIXME: needs_extensions = {'sphinxarg.ext': '0.2'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]
latex_engine = 'xelatex'
