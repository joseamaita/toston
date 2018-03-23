# -*- coding: utf-8 -*-

"""Console script for toston."""

import sys
import click
from toston.toston import seckey


@click.command()
@click.argument('size', type=int)
def main(size):
    """Console script for toston."""
    seckey(size)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
