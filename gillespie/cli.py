import argparse
import logging
import sys
from enum import Enum

from . import gui

LOGGER = logging.getLogger(__name__)


class LogLevels(Enum):
    """
    Log level enumerator.
    """

    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


def create_parser():
    """
    Create a parser for the command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Gillespie simulation of TF chemical reaction system."
    )
    parser.add_argument("--config", type=str, help="Path to the configuration file.")
    # parser.add_argument("--output", type=str, help="Path to the output file.")
    parser.add_argument("--seed", type=int, help="Random seed.", default=None)
    return parser


def main():
    """
    Main function for the command line interface. Parses the arguments and runs the simulation. When the --gui flag is set, the GUI is launched instead of running the simulation and all other arguments are ignored.
    """
    parser = create_parser()
    args = parser.parse_args()

    if not args.config:
        parser.error("Configuration file is required.")

    # Run the simulation


if __name__ == "__main__":
    main()
