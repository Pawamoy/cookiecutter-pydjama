{{ '=' * cookiecutter.project_name|length }}
{{cookiecutter.project_name}}
{{ '=' * cookiecutter.project_name|length }}

.. start-badges


{% if cookiecutter.travis|lower == 'yes' %}
|travis|
{%- endif %}
{%- if cookiecutter.appveyor|lower == 'yes' %}
|appveyor|
{%- endif %}
{%- if cookiecutter.codacy|lower == 'yes' %}
|codacy|
{%- endif %}
{%- if cookiecutter.coveralls|lower == 'yes' %}
|coveralls|
{%- endif %}
{%- if cookiecutter.codecov|lower == 'yes' %}
|codecov|
{%- endif %}
{%- if cookiecutter.landscape|lower == 'yes' %}
|landscape|
{%- endif %}
{%- if cookiecutter.codeclimate|lower == 'yes' %}
|codeclimate|
{%- endif %}
|version|
|wheel|
{%- if cookiecutter.pyup|lower == 'yes' %}
|pyup|
{%- endif %}
{%- if cookiecutter.requiresio|lower == 'yes' %}
|requires|
{%- endif %}
{%- if cookiecutter.gitter|lower == 'yes' %}
|gitter|
{%- endif %}

{% if cookiecutter.travis|lower == 'yes' %}
.. |travis| image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
{% endif %}
{%- if cookiecutter.appveyor|lower == 'yes' %}
.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
{% endif %}
{%- if cookiecutter.requiresio|lower == 'yes' %}
.. |requires| image:: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/requirements/?branch=master
{% endif %}
{%- if cookiecutter.coveralls|lower == 'yes' %}
.. |coveralls| image:: https://coveralls.io/repos/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter.codecov|lower == 'yes' %}
.. |codecov| image:: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
{% endif %}
{%- if cookiecutter.landscape|lower == 'yes' %}
.. |landscape| image:: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master/landscape.svg?style=flat
    :target: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
    :alt: Code Quality Status
{% endif %}
{%- if cookiecutter.codacy|lower == 'yes' %}
.. |codacy| image:: https://api.codacy.com/project/badge/Grade/REPLACE_WITH_PROJECT_ID
    :target: https://www.codacy.com/app/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
    :alt: Codacy Code Quality Status
{% endif %}
{%- if cookiecutter.codeclimate|lower == 'yes' %}
.. |codeclimate| image:: https://codeclimate.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badges/gpa.svg
    :target: https://codeclimate.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
    :alt: CodeClimate Quality Status
{% endif %}
{%- if cookiecutter.pyup|lower == 'yes' %}
.. |pyup| image:: https://pyup.io/repos/github/{{ cookiecutter.github_username|lower }}/{{ cookiecutter.repo_name }}/shield.svg
    :target: https://pyup.io/repos/github/{{ cookiecutter.github_username|lower }}/{{ cookiecutter.repo_name }}/
    :alt: Updates
{% endif %}
{%- if cookiecutter.gitter|lower == 'yes' %}
.. |gitter| image:: https://badges.gitter.im/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
    :alt: Join the chat at https://gitter.im/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    :target: https://gitter.im/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
{% endif %}
.. |version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}/

.. |wheel| image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.distribution_name }}.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}/


.. end-badges

{{ cookiecutter.project_short_description|wordwrap(119) }}

License
=======

Software licensed under `ISC`_ license.

.. _ISC: https://www.isc.org/downloads/software-support-policy/isc-license/

Installation
============

::

    pip install {{ cookiecutter.distribution_name }}

Documentation
=============

http://{{ cookiecutter.repo_name|replace('.', '') }}.readthedocs.io/en/latest/
{# https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name|replace('.', '') }}/wiki #}

Development
===========

To run all the tests: ``tox``
