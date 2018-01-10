all: clean check test report

django18:
	pip install Django>=1.8,<1.9
django19:
	pip install Django>=1.9,<1.10
django110:
	pip install Django>=1.10,<1.11
django111:
	pip install Django>=1.11,<1.12
django20:
	pip install Django>=2.0,<2.1
bandit:
	pip install bandit
safety:
	pip install safety
prospector:
	pip install prospector[with_everything]
pylint:
	pip install pylint
sphinx:
	pip install sphinx sphinx-rtd-theme
spelling:
	pip install sphinxcontrib-spelling
	pip install pyenchant
coverage:
	pip install coverage

check: checksecurity checkstyle checkdocs

checksecurity: bandit safety
	safety check -r requirements/base.txt
	bandit -r src/{{ cookiecutter.package_name }}

checkstyle: pylint
	pylint

checkdocs: docs spelling export SPELLCHECK = 1
	sphinx-build -b spelling -w /dev/null docs dist/docs
	sphinx-build -b linkcheck -w /dev/null docs dist/docs

docs: sphinx
	sphinx-build -E -b html docs dist/docs

coveragereport: coverage
	coverage combine --append
	coverage report
	coverage html

clean:
	rm -rf build
	rm -rf dist
	rm -rf src/*.egg-info
	rm -rf htmlcov
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf .tox
	rm -rf .cache
	rm .coverage
	rm .coverage.*

test: py27 py35 py36 py37

py27: python27
	python -m pytest --cov --cov-report=term-missing -vv tests
	pyenv local --unset

py35: python35
	python -m pytest --cov --cov-report=term-missing -vv tests
	pyenv local --unset

py36: python36
	python -m pytest --cov --cov-report=term-missing -vv tests
	pyenv local --unset

py37: python37
	python -m pytest --cov --cov-report=term-missing -vv tests
	pyenv local --unset


python27:
	pyenv local 2.7.9

python35:
	pyenv local 3.5.4

python36:
	pyenv local 3.6.4

python37:
	pyenv local 3.7-dev
