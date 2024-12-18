from enum import Enum

from .simulation import Simulation


class SupportedInput(Enum):
    """
    Supported input file types.
    """

    CSV = "csv"
    JSON = "json"
    YAML = "yaml"
