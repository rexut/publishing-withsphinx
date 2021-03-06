# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Stephan Linz
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# How to write tests: http://docs.python-guide.org/en/latest/writing/tests/
#

'''
test_sphinx_ext_mathjax
~~~~~~~~~~~~~~~~~~~~~~~

This module contains basic functional tests of the sphinx.ext.mathjax extension
as part of the publishing.withsphinx package.

:copyright: Copyright 2014-2016 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests.functional import fixtures

import re


class TestCaseSphinxExtMathJax(fixtures.TestCaseFunctionalPublishingSphinx):

    @fixtures.with_html_app(
        testroot='ext-math',
        confoverrides={
            'math_number_all': True,
        },
    )
    def test_build_html(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.mathjax: can build html
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.html')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check mathematic equastions
        r = re.compile(
            '(?ms)'
            + re.escape(r'<h2>Test math extensions <span class="')
            + re.escape(self.get_html_class_math() + r'">\(E = m c^2\)</span>')
            + re.escape(r'<a class="headerlink"') + '.*' + re.escape(r'</a></h2>') + '.*'
            + re.escape(r'<div class="' + self.get_html_class_math() + r'"') + '.*'
            + re.escape(r'\[a^2+b^2=c^2\]</div>') + '.*'
            + re.escape(r'<p>Inline <span class="')
            + re.escape(self.get_html_class_math() + r'">\(E=mc^2\)</span></p>')
        )
        self.assertRegex(c, r)

    @fixtures.with_latex_app(
        testroot='ext-math',
        confoverrides={
            'math_number_all': True,
        },
    )
    def test_build_latex(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.mathjax: can build latex
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.tex')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check mathematic equastions
        r = re.compile(
            '(?ms)'
            + re.escape(r'\chapter{Test math extensions ' + self.get_latex_protect())
            + re.escape(r'\(E = m c^2' + self.get_latex_protect() + r'\)}') + '.*'
            + re.escape(r'\begin{split}a^2 + b^2 = c^2\end{split}') + '.*'
            + re.escape(r'Inline \(E=mc^2\)')
        )
        self.assertRegex(c, r)

    @fixtures.with_text_app(
        testroot='ext-math',
        confoverrides={
            'math_number_all': True,
        },
    )
    def test_build_text(self, app, status, warning):
        '''
        FUNCTIONAL TEST: sphinx.ext.mathjax: can build text
        '''
        app.builder.build_update()
        print(status.getvalue())
        print(warning.getvalue())

        p = fixtures.path(app.outdir / 'index.txt')
        self.assertTrue(p.isfile(), 'missing file ' + p)

        c = p.read_text(encoding='utf-8')
        print(c)

        # check mathematic equastions
        r = re.compile(
            '(?ms)'
            + re.escape(r'Test math extensions E = m c^2') + '.*'
            + re.escape(r'a^2+b^2=c^2') + '.*' + re.escape(r'Inline E=mc^2')
        )
        self.assertRegex(c, r)


if __name__ == "__main__":
    fixtures.main()
