""" Shovel Main Tasks file.
"""

import os
from shovel import task  # pylint: disable=import-self


@task
def hello():
    """ Display Hello World!
    """
    print('Hello, World!')


@task
def init():
    """ Initialize the project
    """
    os.system("python -m pip install --upgrade pip")
    os.system("python -m pip install -r python-3-requirements.txt")


@task
def install():
    """ Install the Package locally
    """
    os.system("python setup.py install")


@task
def develop():
    """ Install the develop packages for the project.
    """
    os.system("python setup.py develop")


@task
def test():
    """ Run the tests via setuptools and pytest with pylint and codestyle
    """
    os.system("python setup.py pytest")
