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
|codacygrade|
|codacycoverage|
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
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
    :alt: Travis-CI Build Status
{% endif %}
{%- if cookiecutter.appveyor|lower == 'yes' %}
.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master&svg=true
    :target: https://ci.appveyor.com/project/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
    :alt: AppVeyor Build Status
{% endif %}
{%- if cookiecutter.requiresio|lower == 'yes' %}
.. |requires| image:: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/requirements.svg?branch=master
    :target: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/requirements/?branch=master
    :alt: Requirements Status
{% endif %}
{%- if cookiecutter.coveralls|lower == 'yes' %}
.. |coveralls| image:: https://coveralls.io/repos/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badge.svg?branch=master&service=github
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    :alt: Coverage Status
{% endif %}
{%- if cookiecutter.codecov|lower == 'yes' %}
.. |codecov| image:: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/coverage.svg?branch=master
    :target: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
    :alt: Coverage Status
{% endif %}
{%- if cookiecutter.landscape|lower == 'yes' %}
.. |landscape| image:: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master/landscape.svg?style=flat
    :target: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
    :alt: Code Quality Status
{% endif %}
{%- if cookiecutter.codacy|lower == 'yes' %}
.. |codacygrade| image:: https://api.codacy.com/project/badge/Grade/REPLACE_WITH_PROJECT_ID
    :target: https://www.codacy.com/app/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/dashboard
    :alt: Codacy Code Quality Status

.. |codacycoverage| image:: https://api.codacy.com/project/badge/Coverage/REPLACE_WITH_PROJECT_ID
    :target: https://www.codacy.com/app/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/dashboard
    :alt: Codacy Code Coverage
{% endif %}
{%- if cookiecutter.codeclimate|lower == 'yes' %}
.. |codeclimate| image:: https://codeclimate.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badges/gpa.svg
    :target: https://codeclimate.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
    :alt: CodeClimate Quality Status
{% endif %}
{%- if cookiecutter.pyup|lower == 'yes' %}
.. |pyup| image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/shield.svg
    :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
    :alt: Updates
{% endif %}
.. |version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg?style=flat
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}/
    :alt: PyPI Package latest release

.. |wheel| image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.distribution_name }}.svg?style=flat
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}/
    :alt: PyPI Wheel
{%- if cookiecutter.gitter|lower == 'yes' %}
.. |gitter| image:: https://badges.gitter.im/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
    :target: https://gitter.im/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    :alt: Join the chat at https://gitter.im/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
{% endif %}


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

`On ReadTheDocs`_

.. _`On ReadTheDocs`: http://REPLACE_WITH_RTD_SLUG.readthedocs.io/

Development
===========

To run all the tests: ``tox``
