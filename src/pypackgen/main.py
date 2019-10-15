""" PyPackGen Main Module
"""

import os


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
    open(package_name + '/src/' + package_name + '/__init__.py', 'a').close()
    open(package_name + '/src/' + package_name + '/main.py', 'a').close()

    # Create the tests directory. This is a stylistic choice and what needs to
    # be done because of how the package directory is added in setup.py.
    os.mkdir(package_name + '/test')
    os.mkdir(package_name + '/test/' + package_name)
    open(package_name + '/test/' + package_name + '/__init__.py', 'a').close()
    open(package_name + '/test/' + package_name + '/main_test.py', 'a').close()

    # Shovel is our tasks driver for performing builds and repeated tasks.
    os.mkdir(package_name + '/shovel')
    open(package_name + '/shovel/shovel.py', 'a').close()

    open(package_name + '/LICENSE.md', 'a').close()

    open(package_name + '/README.md', 'a').close()

    open(package_name + '/setup.py', 'a').close()

    open(package_name + '/setup.cfg', 'a').close()

    open(package_name + '/python-3-requirements.txt', 'a').close()
