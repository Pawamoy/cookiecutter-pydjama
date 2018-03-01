# Cookiecutter-Pydjama

<!-- badge list -->
Opinionated cookiecutter to create Python and Django projects.

<!-- logo -->

- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Features](#features)
- [License: ISC License](LICENSE)
- [Requirements](#requirements)
- [Usage](#usage)
- [Credits](#credits)

## Features
**Documentation**
- Documentation with [Sphinx][], [ReadTheDocs][] theme
  and Markdown thanks to [recommonmark][].

**Frameworks**
- Support for [Django][] apps (not projects).

**Licenses**
- All licenses from [choosealicense.com][].

**Publishing**
- Publishing done with [flit][].

**Tests**
- [tox][] for multiple Python version testing.
- [pytest][] for running tests.
- Optional [django-fake-model][] dependency for tests.

**Tools**
- [isort][] to quickly sort imports with `isort -y -rc src`.
- [bumpversion][] to manage version number across files.
- [pylint][] for static code analysis.
- [bandit][] for security analysis.
- [safety][] to check your dependencies (updates and vulnerabilities).

## Requirements
- [git][]
- [python][]
- [cookiecutter][]

## Usage
```
cookiecutter gh:Pawamoy/cookiecutter-pydjama
```

Tip: to be able to update your generated project whenever this cookiecutter
receives updates, you should immediately create a "cookiecutter" or "template"
branch. Then when you want to update it, checkout the "cookiecutter" branch
and run:

```
cookiecutter --overwrite-if-exists --no-input \
  --config-file .cookiecutterrc \
  --output-dir .. gh:Pawamoy/cookiecutter-pydjama
```

Now you can commit the changes to your "cookiecutetr" branch and merge them
in your "master" branch without too much conflicts.


## Credits
This cookiecutter was created with [cookiecutter-cookiecutter]().
It also got a lot of inspiration from [cookiecutter-pylibrary][],
[cookiecutter-pypackage][] and [cookiecutter-djangopackage][].


[bumpversion]: https://pypi.python.org/pypi/bumpversion
[choosealicense.com]: https://choosealicense.com/appendix/
[cookiecutter]: https://github.com/audreyr/cookiecutter
[cookiecutter-djangopackage]: https://github.com/pydanny/cookiecutter-djangopackage
[cookiecutter-cookiecutter]: https://github.com/Pawamoy/cookiecutter-cookiecutter
[cookiecutter-pylibrary]: https://github.com/ionelmc/cookiecutter-pylibrary
[cookiecutter-pypackage]: https://github.com/audreyr/cookiecutter-pypackage
[Django]: https://www.djangoproject.com/
[django-fake-model]: https://github.com/erm0l0v/django-fake-model
[git]: https://git-scm.com/downloads
[isort]: https://pypi.python.org/pypi/isort
[pylint]: https://github.com/PyCQA/pylint
[pytest]: http://pytest.org/
[python]: https://www.python.org/downloads/
[ReadTheDocs]: https://readthedocs.org/
[recommonmark]: https://github.com/rtfd/recommonmark
[Sphinx]: http://sphinx-doc.org/
[tox]: http://testrun.org/tox/
