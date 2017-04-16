#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Setup script.

Uses setuptools.
Long description is a concatenation of README.rst and CHANGELOG.rst.
"""

from __future__ import absolute_import, print_function

import io
import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    """Read a file in current directory."""
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='{{ cookiecutter.distribution_name }}',
    version='{{ cookiecutter.version }}',
    license='ISC',
    description={{ '{0!r}'.format(cookiecutter.project_short_description).lstrip('ub') }},
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S)
        .sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author={{ '{0!r}'.format(cookiecutter.full_name).lstrip('rb') }},
    author_email={{ '{0!r}'.format(cookiecutter.email).lstrip('ub') }},
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: Unix',{% if cookiecutter.django|lower == "yes" %}
        'Framework :: Django',{% if '1.8' in cookiecutter.django_versions %}
        # 'Framework :: Django :: 1.8',{% endif %}{% if '1.9' in cookiecutter.django_versions %}
        # 'Framework :: Django :: 1.9',{% endif %}{% if '1.10' in cookiecutter.django_versions %}
        # 'Framework :: Django :: 1.10',{% endif %}{% if '1.11' in cookiecutter.django_versions %}
        # 'Framework :: Django :: 1.11',{% endif %}{% endif %}
        'Programming Language :: Python',{% if '2.6' in cookiecutter.python_versions %}
        'Programming Language :: Python :: 2.6',{% endif %}{% if '2.7' in cookiecutter.python_versions %}
        'Programming Language :: Python :: 2.7',{% endif %}
        'Programming Language :: Python :: 3',{% if '3.2' in cookiecutter.python_versions %}
        'Programming Language :: Python :: 3.2',{% endif %}{% if '3.3' in cookiecutter.python_versions %}
        'Programming Language :: Python :: 3.3',{% endif %}{% if '3.4' in cookiecutter.python_versions %}
        'Programming Language :: Python :: 3.4',{% endif %}{% if '3.5' in cookiecutter.python_versions %}
        'Programming Language :: Python :: 3.5',{% endif %}{% if '3.6' in cookiecutter.python_versions %}
        'Programming Language :: Python :: 3.6',{% endif %}{% if 'pypy' in cookiecutter.python_versions %}
        'Programming Language :: Python :: Implementation :: PyPy',{% endif %}
        'Topic :: Utilities',
    ],
    keywords=[
        '{{ cookiecutter.repo_name }}',
    ],
    install_requires=[
{%- if cookiecutter.command_line_interface|lower == 'click' %}
        'click',
{%- else %}
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
{%- endif %}
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
{%- if cookiecutter.command_line_interface|lower != 'no' %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.command_line_interface_bin_name }} = {{ cookiecutter.package_name|replace('-', '_') }}.cli:main',
        ]
    },
{%- endif %}
)
