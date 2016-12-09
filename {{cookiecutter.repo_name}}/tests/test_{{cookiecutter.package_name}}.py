# -*- coding: utf-8 -*-

"""Main test script."""

{% if cookiecutter.django|lower == "yes" %}

from django.test import TestCase

import {{ cookiecutter.package_name }}


class MainTestCase(TestCase):
    """Main Django test case."""

    def setUp(self):
        """Setup method."""
        pass

    def test_main(self):
        """Main test method."""
        assert {{ cookiecutter.package_name }}

    def tearDown(self):
        """Tear down method."""
        pass

{%- else %}

{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner

from {{ cookiecutter.package_name }}.cli import main
{%- elif cookiecutter.command_line_interface|lower in ['plain', 'argparse'] %}
from {{ cookiecutter.package_name }}.cli import main
{%- else %}

import {{ cookiecutter.package_name }}
{%- endif %}


def test_main():
    """Main test method."""
{% if cookiecutter.command_line_interface|lower == 'click' %}
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0
{%- elif cookiecutter.command_line_interface|lower == 'argparse' %}
    main([])
{%- elif cookiecutter.command_line_interface|lower == 'plain' %}
    assert main([]) == 0
{%- else %}
    assert {{ cookiecutter.package_name }}  # use your library here
{%- endif %}

{%- endif %}
