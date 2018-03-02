# -*- coding: utf-8 -*-

"""Main test script."""

{% if cookiecutter.package_uses_django|lower == "yes" %}
from django.test import TestCase

import {{ cookiecutter.package_import_name }}


class MainTestCase(TestCase):
    """Main Django test case."""

    def setUp(self):
        """Setup method."""
        self.package = {{ cookiecutter.package_import_name }}

    def test_main(self):
        """Main test method."""
        assert self.package

    def tearDown(self):
        """Tear down method."""
        del self.package


{%- else %}

{%- if cookiecutter.package_cli_library|lower == 'click' %}
from click.testing import CliRunner

from {{ cookiecutter.package_import_name }}.cli import main
{%- elif cookiecutter.package_cli_library|lower in ['plain', 'argparse'] %}
from {{ cookiecutter.package_import_name }}.cli import main
{%- else %}

import {{ cookiecutter.package_import_name }}
{%- endif %}

def test_main():
    """Main test method."""
{%- if cookiecutter.package_cli_library|lower == 'click' %}
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0
{%- elif cookiecutter.package_cli_library|lower == 'argparse' %}
    main([])
{%- elif cookiecutter.package_cli_library|lower == 'plain' %}
    assert main([]) == 0
{%- else %}
    assert {{ cookiecutter.package_import_name }}  # use your library here
{%- endif %}

{%- endif %}
