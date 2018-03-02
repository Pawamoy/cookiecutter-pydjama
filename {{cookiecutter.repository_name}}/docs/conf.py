# -*- coding: utf-8 -*-

"""Sphinx configuration file."""

from __future__ import unicode_literals

import os

from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

{% if cookiecutter.package_uses_django|lower == "yes" -%}
import sys
import django
from django.conf import settings

sys.path.insert(0, os.path.join(os.path.abspath('..'), 'src'))
settings.configure(
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sites',
    ],
    SITE_ID=1
)
django.setup()
{%- endif %}

source_parsers = {
    '.md': CommonMarkParser,
}

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

autodoc_default_flags = [
    'members',
    'special-members',
    'show-inheritance'
]

if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

source_suffix = ['.rst', '.md']
master_doc = 'index'
project = {{ '{0!r}'.format(cookiecutter.project_name) }}
year = '{{ cookiecutter.copyright_date }}'
author = {{ '{0!r}'.format(cookiecutter.author_fullname) }}
copyright = '{0}, {1}'.format(year, author)
version = release = '0.1.0'

provider_root = 'https://{{ cookiecutter.repository_provider }}/{{ cookiecutter.repository_namespace }}/{{ cookiecutter.repository_name }}'
pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': ('{}/issues/%s'.format(provider_root), '#'),
}

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only set the theme if we're building docs locally
    html_theme = 'sphinx_rtd_theme'

html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)

html_context = {
    'extra_css_files': [
        '_static/extra.css',
    ],
}

html_static_path = [
    "extra.css",
]

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
suppress_warnings = ["image.nonlocal_uri"]

provider_doc_root = provider_root + '/blob/master/'


def setup(app):
    app.add_config_value(
        'recommonmark_config', {
            'enable_auto_toc_tree': True,
            'auto_toc_tree_section': "Welcome to {{ cookiecutter.project_name|replace('"', '\\"') }}'s documentation!",
            'url_resolver': lambda url: provider_doc_root + url
        }, True)
    app.add_transform(AutoStructify)
