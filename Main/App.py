#!/usr/bin/env python
"""CLI interface for Gillerspie w/ GUI"""

import argparse
import logging
import sys
from enum import Enum

from .GUI.Interface import Root
from Version import __version__

LOGGER = logging.getLogger(__name__)


class LogLevels(Enum):
    """Log level enumerator."""

    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments.

    Returns:
        Parsed CLI arguments.
    """
    # set metadata
    description = f"{sys.modules[__name__].__doc__}\n\n" ""
    epilog = (
        f"%(prog)s v{__version__}, (c) 2024 by Group C"
        "(zavolab-biozentrum@unibas.ch)"
    )

    # instantiate parser
    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # add arguments
    parser.add_argument(
        "--i",
        nargs=1,
        type=str,
        metavar="inputPath",
        help="Path to the configuration file",
    )
    parser.add_argument(
        "--o",
        choices=[e.name for e in LogLevels],
        default=LogLevels.INFO.name,
        metavar="OutputPath",
        type=int,
        help="logging verbosity level",
    )
    parser.add_argument(
        "--s",
        choices=[e.name for e in LogLevels],
        default=LogLevels.INFO.name,
        metavar="Steps",
        type=int,
        help="logging verbosity level",
    )
    parser.add_argument(
        "--t",
        choices=[e.name for e in LogLevels],
        default=LogLevels.INFO.name,
        metavar="Trajectories",
        type=int,
        help="logging verbosity level",
    )


    # return parsed arguments
    return parser.parse_args()


def setup_logging(verbosity: str = "INFO") -> None:
    """Configure logging.

    Args:
        verbosity: Level of logging verbosity.
    """
    level = LogLevels[verbosity].value
    logging.basicConfig(
        level=level,
        format="[%(asctime)s %(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main() -> None:
    """Entry point for CLI executable."""
    args = parse_args()
    setup_logging(verbosity=args.verbosity)
    LOGGER.debug(f"CLI arguments: {args}")

    app = Root()  # Assuming Root is the main Tkinter window class

    LOGGER.info("GUI closed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
