from __future__ import print_function

import datetime
import os
from os.path import join
from collections import OrderedDict

try:
    from click.termui import secho
except ImportError:
    warn = print
else:
    def warn(text):
        for line in text.splitlines():
            secho(line, fg="white", bg="red", bold=True)


try:
    import yaml


    def ordered_load(stream, Loader=yaml.SafeLoader, object_pairs_hook=OrderedDict):
        class OrderedLoader(Loader):
            pass

        def construct_mapping(loader, node):
            loader.flatten_mapping(node)
            return object_pairs_hook(loader.construct_pairs(node))

        OrderedLoader.add_constructor(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            construct_mapping)
        return yaml.load(stream, OrderedLoader)


    def ordered_dump(data, stream=None, Dumper=yaml.SafeDumper, **kwds):
        class OrderedDumper(Dumper):
            pass

        def _dict_representer(dumper, data):
            return dumper.represent_mapping(
                yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                data.items())

        OrderedDumper.add_representer(OrderedDict, _dict_representer)
        return yaml.dump(data, stream, OrderedDumper, **kwds)


    def lint_yaml(yaml_file):
        with open(yaml_file) as f:
            contents = ordered_load(f)
        with open(yaml_file, 'w') as f:
            ordered_dump(contents, f)

except ImportError:
    def lint_yaml(yaml_file):
        print('Yaml is not available, not linting %s' % yaml_file)


def lint_ini(ini_file):
    try:
        from configparser import ConfigParser
    except ImportError:
        try:
            from ConfigParser import ConfigParser
        except ImportError:
            print('ConfigParser is not available, not linting %s' % ini_file)
            return
    config = ConfigParser()
    config.read(ini_file)
    with open(ini_file, 'w') as f:
        config.write(f)


def replace_contents(filename, what, replacement):
    with open(filename) as fh:
        changelog = fh.read()
    with open(filename, 'w') as fh:
        fh.write(changelog.replace(what, replacement))

if __name__ == "__main__":
    today = datetime.date.today()
    replace_contents('CHANGELOG.rst', '<TODAY>', today.strftime("%Y-%m-%d"))
    replace_contents('docs/conf.py', '<YEAR>', str(today.year))
    replace_contents('LICENSE', '<YEAR>', str(today.year))

    lint_ini('tox.ini')
    replace_contents('tox.ini', '\t', '    ')
    lint_ini('setup.cfg')
    replace_contents('setup.cfg', '\t', '    ')

{%- if cookiecutter.command_line_interface|lower == 'no' %}
    os.unlink(join('src', '{{ cookiecutter.package_name|replace('-', '_') }}', '__main__.py'))
    os.unlink(join('src', '{{ cookiecutter.package_name|replace('-', '_') }}', 'cli.py'))
{% endif %}

{%- if cookiecutter.django|lower == 'no' %}
    os.unlink('runtests.py')
{% endif %}

{%- if cookiecutter.appveyor|lower == 'no' %}
    os.unlink('appveyor.yml')
{% else %}
    lint_yaml('appveyor.yml')
{% endif %}

{%- if cookiecutter.travis|lower == 'no' %}
    os.unlink('.travis.yml')
{% else %}
    lint_yaml('.travis.yml')
{% endif %}

{%- if cookiecutter.pyup|lower == 'no' %}
    os.unlink('.pyup.yml')
{% endif %}

    print("""
You have succesfully created `{{ cookiecutter.repo_name }}`
with these cookiecutter parameters:

{% for key, value in cookiecutter.items()|sort %}
  {{ "{0:32}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}

--------------

To get started run these:

  cd {{ cookiecutter.repo_name }}
  git init
  git add --all
  git commit -m "Add initial project skeleton."
  git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git
  git push -u origin master
  git checkout -b template  # enable updating from cookiecutter
  git push --set-upstream origin template

Remember to enable continuous integration, documentation generation
and online code health check before your first push ;)

Use './update.sh . gh:Pawamoy/cookiecutter-pydjama' to update your project
with the last changes of pydjama.
""")

    command_line_interface_bin_name = '{{ cookiecutter.command_line_interface_bin_name }}'
    while command_line_interface_bin_name.endswith('.py'):
        command_line_interface_bin_name = command_line_interface_bin_name[:-3]

        if command_line_interface_bin_name == '{{ cookiecutter.package_name|replace('-', '_') }}':
            warn("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!                                                                            !!
!!  WARNING:                                                                  !!
!!                                                                            !!
!!    Your result package is broken. Your bin script named                    !!
!!    {0}
!!                                                                            !!
!!    Python automatically adds the location of scripts to                    !!
!!    `sys.path`. Because of that, the bin script will fail                   !!
!!    to import your package because it has the same name                     !!
!!    (it will try to import itself as a module).                             !!
!!                                                                            !!
!!    To avoid this problem you have two options:                             !!
!!                                                                            !!
!!    * Remove the ".py" suffix from the `command_line_interface_bin_name`.   !!
!!                                                                            !!
!!    * Use a different `package_name` {1}
!!                                                                            !!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""".format(
                '"{{ cookiecutter.command_line_interface_bin_name }}" will shadow your package.'.ljust(65),
                '(not "{0}").'.format(command_line_interface_bin_name).ljust(32)))
        break
