from .simulation import Simulation

from enum import Enum


class SupportedInput(Enum):
    """
    Supported input file types.
    """

    CSV = "csv"
    JSON = "json"
    YAML = "yaml"
