import os
import shutil

from jinja2 import Environment, FileSystemLoader


def get_context():
    """As hooks are executed rendered, it will return a context dict."""
    context = {"cookiecutter": {
    {%- for key, value in cookiecutter.items()|sort %}
        "{{ key }}": {{ "{0!r}".format(value) }},
    {% endfor -%}
    } }
    return context


def render_template(source, target):
    """Utility function to render a source template in a target file."""
    env = Environment(loader=FileSystemLoader('.'), keep_trailing_newline=True)
    template = env.get_template(source)
    context = get_context()
    rendered = template.render(context)
    with open(target, 'w') as stream:
        stream.write(rendered)


def render_license():
    """Render the selected license in the LICENSE file."""
    target = 'LICENSE'
    source = os.path.join(
        'licenses',
        '{{ cookiecutter.copyright_license }}'
            .replace('"', '')
            .replace("'", '')
            .replace('/', '-')
            .replace(' ', '_'))

    render_template(source, target)
    shutil.rmtree('licenses')


def print_context():
    """Simply print the context in a pretty manner."""
    print("""
    You have succesfully created `{{ cookiecutter.repository_name }}`
    with these cookiecutter parameters:

    {% for key, value in cookiecutter.items()|sort %}
      {{ "{0:28}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
    {%- endfor %}
    """)


render_license()
print_context()
