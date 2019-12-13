# pypackgen

## Overview

A Python Package to generate Python Packages the way I like them. Ths is because
I could never find an actual Python project to generate these things and I hated
creating them by hand. If anyone has anything to show me, please do and I'll
immediately use that.

## Requirements

* Python 3.6 or newer with Pip

## Setup

Install the base packages

```bash
python -m pip install --upgrade pip
python -m pip install -r python-3-requirements.txt
```

Install from source:

```bash
python setup.py install
```

Or install from PyPi, if I ever get it published.

```bash
python -m pip install pypackgen
```

## Usage

Run the executable TODO

```bash
pypackgen mytestmodule
```

Providing no name will yield in the default package name. No one wants that. This should produce something similar to...

```bash
(pypackgen) ➜  mytestmodule tree .
.
├── LICENSE.md
├── python-3-requirements.txt
├── README.md
├── setup.cfg
├── setup.py
├── shovel
│   └── shovel.py
├── src
│   └── mytestmodule
│       ├── __init__.py
│       └── main.py
└── test
    └── mytestmodule
        ├── __init__.py
        └── main_test.py

5 directories, 10 files
```

## Documentation

To generate the documentation for the Python Package, use Sphinx. The commands
will be included in the shovel tasks file to make it easy. However, this does
require that GNU Make is installed.

```bash
shovel sphinx
```

## Development and Testing

I am using Setuptools to execute Pytest which then calls Pylint and pycodestyle
to perform testing. That way its all concise single points to go through. I
have also included a `Makefile` and a series of `shovel` tasks.

Make sure to fork the repository. Then create a branch of master. Then run the
tests and add more for features being added. Once satisfied, push to your Fork
and then open a Pull Request to the upstream master.

## References

* [Python Packaging Tutorial](https://packaging.python.org/tutorials/packaging-projects/)
* [Python 3 Modules and Imports](https://docs.python.org/3/tutorial/modules.html#packages)
* [Python setup.py](https://docs.python.org/3/distutils/setupscript.html)
* [Setuptools Documentation](https://setuptools.readthedocs.io/en/latest/setuptools.html)
* [NumPy DocString examples](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html)
* [How to create custom commands and extend existing commands](https://jichu4n.com/posts/how-to-add-custom-build-steps-and-commands-to-setuppy/)
* [PyTest Good Practices setup](http://doc.pytest.org/en/latest/goodpractices.html)
