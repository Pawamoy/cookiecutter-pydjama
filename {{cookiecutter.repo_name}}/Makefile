TOX = tox

all:
	$(TOX) -e clean,setup,safety,style,docs,
		{%- for py in ["2.7", "3.5", "3.6", "3.7-dev"] -%}
			{%- if py in cookiecutter.python_versions.split(',') -%}
				{%- if cookiecutter.django|lower == "yes" -%}
					{%- for dj in cookiecutter.django_versions.split(',') -%}py{{ py|replace(".", "") }}-django{{ dj|replace(".", "") }},{% endfor -%}
				{%- else -%}py{{ py|replace(".", "") }},{%- endif -%}
			{%- endif -%}
		{%- endfor -%},report

all_parallel: TOX = detox
all_parallel: all

check:
	$(TOX) -e setup,safety,style,docs

check_parallel: TOX = detox
check_parallel: check

test:
	tox -e clean
	$(TOX) -e
	  {%- for py in ["2.7", "3.5", "3.6", "3.7-dev"] -%}
			{%- if py in cookiecutter.python_versions.split(',') -%}
				{%- if cookiecutter.django|lower == "yes" -%}
					{%- for dj in cookiecutter.django_versions.split(',') -%}py{{ py|replace(".", "") }}-django{{ dj|replace(".", "") }},{% endfor -%}
				{%- else -%}py{{ py|replace(".", "") }},{%- endif -%}
			{%- endif -%}
		{%- endfor %}
	tox -e report

test_parallel: TOX = detox
test_parallel: test
