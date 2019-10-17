""" Click Executable Script
"""

import click
import pypackgen.main as pypackgen

# pylint: disable=no-value-for-parameter


@click.command()
@click.argument('package_name', default='python_package')
def cli(package_name):
    """ cli, the exectuable for this package
    """
    pypackgen.create_package(package_name)
    print("Python Package structure created.")


if __name__ == '__main__':
    cli()
