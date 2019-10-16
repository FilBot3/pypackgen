""" PyPackGen Main Module
"""

import os
import jinja2

def create_readme(package_name):
    """Creates the README.md for the package
    """
    template_contents = '''# {{ package_name }}

## Overview

The {{ package_name }} does this. Fill this part out to give more information
about what it is supposed to do.

## Requirements

* Python 3.6 or newer with Pip

## Setup

Update Pip. There are instances where this isn't good or doable, YMMV.

```bash
python -m pip install --upgrade pip
```

Install the Python required packages.

```bash
python -m pip install -r python-3-requirements.txt
```

Install the module in development mode.

```bash
python setup.py develop
```

## Usage

TODO: Give usage examples. 

Used as a library

```python
import {{ package_name }}
```

Used as an executable

```bash
{{ package_name }} --help
```

## Development

Use the [Git Forking Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow) to create a working copy. Then perform development and then open a Pull Request. If you have access to the repository, use the [Git Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) and open Pull Requests.

## References

* [Python Setuptools](https://setuptools.readthedocs.io/)
* [Python Pip](https://docs.python.org/3/installing/index.html)
    '''

    template_values = {
        'package_name': package_name,
    }

    template_file = open(package_name + '/README.md', 'w+')
    template_file.write(jinja2.Template(template_contents).render(template_values))
    template_file.close()


def create_init(package_name, location):
    """Creates __init__.py files
    """
    template_contents = '''"""__init__.py
"""
    '''

    template_values = {}

    template_file = open(package_name + location + package_name + '/__init__.py', 'w+')
    template_file.write(jinja2.Template(template_contents).render(template_values))
    template_file.close()


def create_main(package_name):
    """Create main.py
    """
    template_contents = '''""" main.py
"""

def hello():
    """Returns hello world
    """
    return 'Hello, World!'


if __name__ == '__main__':
    print(hello())
    '''

    template_values = {}

    template_file = open(package_name + '/src/' + package_name + '/main.py', 'w+')
    template_file.write(jinja2.Template(template_contents).render(template_values))
    template_file.close()


def create_main_test(package_name):
    """Creates the main_test.py
    """
    template_contents = '''"""main_test.py
"""
    '''

    template_values = {}

    template_file = open(package_name + '/test/' + package_name + '/main_test.py', 'w+')
    template_file.write(jinja2.Template(template_contents).render(template_values))
    template_file.close()


def create_license(package_name):
    """Creates the LICENSE.md
    """
    template_contents = '''MIT License

Copyright (c) 2019 The Authors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
    '''

    template_values = {}

    template_file = open(package_name + '/LICENSE.md', 'w+')
    template_file.write(jinja2.Template(template_contents).render(template_values))
    template_file.close()


def create_changelog(package_name):
    """Creates the CHANGELOG.md
    """
    template_contents = '''# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

    ## [Unreleased]
    '''

    template_values = {}

    template_file = open(package_name + '/CHANGELOG.md', 'w+')
    template_file.write(jinja2.Template(template_contents).render(template_values))
    template_file.close()


def create_shovel(package_name):
    """Creates the shovel/shovel.py Task runner
    """
    template_contents = '''"""Shovel Task File
"""

from shovel import task

@task
def hello():
    """Prints Hello, World
    """
    print('Hello, World!')
    '''

    template_values = {}

    template_file = open(package_name + '/shovel/shovel.py', 'w+')
    template_file.write(jinja2.Template(template_contents).render(template_values))
    template_file.close()


def create_setupcfg(package_name):
    """Creates the setup.cfg
    """
    template_contents = '''# vim: ft=dosini

[tool:pytest]
addopts = --pylint --codestyle
    '''

    template_values = {}

    template_file = open(package_name + '/setup.cfg', 'w+')
    template_file.write(jinja2.Template(template_contents).render(template_values))
    template_file.close()


def create_setuppy(package_name):
    """Creates the setup.py
    """
    template_contents = '''""" setuptools setup.py
"""

import setuptools


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()


setuptools.setup(
    name="{{ package_name }}",
    version="0.0.1",
    author="Author Name",
    author_email="AuthorEmail@email.com",
    description="Replace this with a short description",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/[USERNAME]/{{ package_name }}",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite='test.{{ package_name }}',
    tests_require=[
        "autopep8",
        "pycodestyle",
        "pylint",
        "pytest",
        "pytest-codestyle",
        "pytest-pylint",
        "pytest-runner",
    ],
    install_requires=[],
)
    '''

    template_values = {
        'package_name': package_name,
    }

    template_file = open(package_name + '/setup.py', 'w+')
    template_file.write(jinja2.Template(template_contents).render(template_values))
    template_file.close()


def create_python_requirements(package_name):
    """Creates the python-3-requirements.txt
    """
    template_contents = '''autopep8
pycodestyle
pylint
pytest
pytest-codestyle
pytest-pylint
pytest-runner
setuptools
shovel
virtualenv
    '''

    template_values = {}

    template_file = open(package_name + '/python-3-requirements.txt', 'w+')
    template_file.write(jinja2.Template(template_contents).render(template_values))
    template_file.close()


def create_package(package_name='python_module'):
    """pypackgen.main.create_package()

    This function simply creates a skeleton directory structure and files that
    are used in Python Module/Package development. It saves me time having to
    recreate these everytime I want to make a Python Module/Package to test
    something out. It gets quite annoying having to redo this over and over.

    Parameters
    ----------
    package_name : str
        The name of the package. Will default to 'python_module' if none is
        supplied. If supplied, will use that name instead.

    .. _PEP-484:
        https://www.python.org/dev/peps/pep0484/
    """
    # Create the main package sources directory.
    os.mkdir(package_name)
    os.mkdir(package_name + '/src')
    os.mkdir(package_name + '/src/' + package_name)
    create_init(package_name, '/src/')
    create_main(package_name)

    # Create the tests directory. This is a stylistic choice and what needs to
    # be done because of how the package directory is added in setup.py.
    os.mkdir(package_name + '/test')
    os.mkdir(package_name + '/test/' + package_name)
    create_init(package_name, '/test/')
    create_main_test(package_name)

    # Shovel is our tasks driver for performing builds and repeated tasks.
    os.mkdir(package_name + '/shovel')
    create_shovel(package_name)

    create_license(package_name)

    create_readme(package_name)

    create_setuppy(package_name)

    create_setupcfg(package_name)

    create_python_requirements(package_name)
