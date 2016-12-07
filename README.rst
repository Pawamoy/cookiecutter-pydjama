====================
cookiecutter-pydjama
====================

This cookiecutter is originally a fork of `cookiecutter-pylibrary`_, but it also
combines features from `cookiecutter-pypackage`_ and `cookiecutter-djangopackage`_.

It fits really well my needs, but maybe not yours, so don't hesitate to fork it.

Features
--------

* Support for Django_, tests with `django-fake-model`_.
* Mozilla Public License 2.0.
* Tox_ for managing test environments for Python 2.7, 3.3, PyPy etc.
* Pytest_ for testing Python 2.7, 3.3, PyPy etc.
* Travis-CI_ and AppVeyor_ for continuous testing.
* Coveralls_ or Codecov_ for coverage tracking (using Tox_).
* Documentation with Sphinx_, ready for ReadTheDocs_ (soon).
* Configurations for isort_,  bumpversion_, yapf_ and prospector_.
* Packaging and code quality checks. This template comes with a tox environment (``check``) that will:

  * Check if your ``README.rst`` is valid.
  * Check if the ``MANIFEST.in`` has any issues.
  * Run ``flake8`` (a combo of PEP8, pyflakes and McCabe checks)
  * Run ``prospector`` (landscape tool, soon).

* Badges for everything in README.rst, including PyUp_, Landscape_ and Gitter_.
* Script to easily release code to PyPiTest and PyPi.
* Script to easily update your generated project when the cookiecutter changes. To enable this,
  you wil need to create a ``template`` branch in the repository.

Requirements
------------

Projects using this template have these minimal dependencies:

* Cookiecutter_ - just for creating the project
* Tox_ - for running the tests
* Setuptools_ - for building the package, wheels etc.
* Twine_ to register and upload the code to PyPiTest and PyPi.

::

  pip install tox cookiecutter twine


Usage and options
-----------------

First generate your project::

  cookiecutter gh:Pawamoy/cookiecutter-pydjama

After this you can create the initial repository (make sure you `create <https://github.com/new>`_ an *empty* Github
project)::

  git init .
  git add .
  git commit -m "Initial skel."
  git remote add origin git@github.com:username/reponame.git
  git push -u origin master
  git checkout -b template
  git push --set-upstream origin template

Then:

* Enable the repository in your Travis, Codecov, Coveralls, Landscape, Gitter, ReadTheDocs accounts
* For ReadTheDocs: turn on the ReadTheDocs service hook.
  Don't forget to enable virtualenv and specify ``docs/requirements.txt``
  as the requirements file in ``Advanced Settings``.

Developing the project
``````````````````````

To run all the tests, just run::

  tox

To see all the tox environments::

  tox -l

To only build the docs::

  tox -e docs

To build and verify that the built package is proper and other code QA checks::

  tox -e check

Releasing the project
`````````````````````
Before releasing your package on PyPI you should have all the tox environments passing.

Version management
''''''''''''''''''

This template provides a basic bumpversion_ configuration. It's as simple as running:

* ``bumpversion patch`` to increase version from `1.0.0` to `1.0.1`.
* ``bumpversion minor`` to increase version from `1.0.0` to `1.1.0`.
* ``bumpversion major`` to increase version from `1.0.0` to `2.0.0`.

You should read `Semantic Versioning 2.0.0 <http://semver.org/>`_ before bumping versions.

Building and uploading
''''''''''''''''''''''

Store your credentials in a ``.pypirc`` file in your home.

.. code::

    [distutils]
    index-servers =
      pypi
      pypitest

    [pypi]
    repository=https://pypi.python.org/pypi
    username=your_username
    password=your_password

    [pypitest]
    repository=https://testpypi.python.org/pypi
    username=your_username
    password=your_password

Then just run ``./release.sh``. It ``tox -e check`` succeeds, then the script will successively try
to register then upload on PyPiTest first then PyPi server. If any of these steps fails, the
script stops.

Changelog
---------

See `CHANGELOG.rst <https://github.com/Pawamoy/cookiecutter-pydjama/blob/master/CHANGELOG.rst>`_.


.. _AppVeyor: http://www.appveyor.com/
.. _bumpversion: https://pypi.python.org/pypi/bumpversion
.. _Codacy: https://codacy.com/
.. _CodeClimate: https://codeclimate.com/
.. _Codecov: http://codecov.io/
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-pylibrary`: https://github.com/ionelmc/cookiecutter-pylibrary
.. _`cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _Coveralls: https://coveralls.io/
.. _`django-fake-model`: https://github.com/erm0l0v/django-fake-model
.. _Gitter: https://gitter.im
.. _isort: https://pypi.python.org/pypi/isort
.. _Landscape: https://landscape.io
.. _Landscape: https://landscape.io/
.. _Nose: http://nose.readthedocs.org/
.. _Pytest: http://pytest.org/
.. _PyUp: https://pyup.io/
.. _ReadTheDocs: https://readthedocs.org/
.. _`requires.io`: https://requires.io/
.. _Scrutinizer: https://scrutinizer-ci.com/
.. _Setuptools: https://pypi.python.org/pypi/setuptools
.. _Sphinx: http://sphinx-doc.org/
.. _Tox: http://testrun.org/tox/
.. _Travis-CI: http://travis-ci.org/
.. _Twine: https://pypi.python.org/pypi/twine
.. _yapf: https://github.com/google/yapf
