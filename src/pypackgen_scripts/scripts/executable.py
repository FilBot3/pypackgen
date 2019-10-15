""" Click Executable Script
"""

import click
import pypackgen.main as pypackgen


@click.command()
def cli():
    """ cli, the exectuable for this package
    """
    pypackgen.create_package()
    print("Python Package structure created.")


if __name__ == '__main__':
    cli()
