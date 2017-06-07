# -*- coding: utf-8 -*-

"""Sphinx configuration file."""

from __future__ import unicode_literals

import os

{% if cookiecutter.django|lower == "yes" -%}
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

source_suffix = '.rst'
master_doc = 'index'
project = {{ '{0!r}'.format(cookiecutter.project_name) }}
year = '<YEAR>'
author = {{ '{0!r}'.format(cookiecutter.full_name) }}
copyright = '{0}, {1}'.format(year, author)
version = release = {{ '{0!r}'.format(cookiecutter.version) }}

pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': ('https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues/%s', '#'),
    'pr': ('https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/pull/%s', 'PR #'),
}

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only set the theme if we're building docs locally
    html_theme = 'sphinx_rtd_theme'

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
