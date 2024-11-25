#!/usr/bin/env python
"""CLI interface for Gillerspie Simulation"""
import argparse
import logging
import sys
from enum import Enum

from Main.GUI.Interface import SceneTree
import Projectconfiguration

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
        f"%(prog)s v{Projectconfiguration.VERSION}, (c) 2024 by {Projectconfiguration.AUTHOR}"
        f"({Projectconfiguration.MAIL})"
    )

    # instantiate parser
    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # add arguments
    parser.add_argument(
        "numbers",
        nargs=2,
        type=int,
        metavar="INT",
        help="exactly two numbers that arithmetics operations are applied on",
    )
    parser.add_argument(
        "--verbosity",
        choices=[e.name for e in LogLevels],
        default=LogLevels.INFO.name,
        type=str,
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
    app = SceneTree()  # Assuming Root is the main Tkinter window class 

    LOGGER.info("GUI closed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
