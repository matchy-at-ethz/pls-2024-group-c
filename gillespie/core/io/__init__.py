from pathlib import Path
from typing import Any, Dict

from .. import SupportedInput
from . import csv_parser, json_parser, yaml_parser


def parse(file_name: str | Path) -> Dict[str, Any]:
    """
    Parse a configuration file and return the configuration as a dictionary.

    Args:
        file_name: Path to the configuration file.

    Returns:
        A dictionary with the configuration.
    """
    file_path = Path(file_name)
    if not file_path.exists():
        raise FileNotFoundError(f"Configuration file {file_path} not found.")

    file_extension = file_path.suffix.lstrip(".")

    match file_extension:
        case SupportedInput.CSV.value:
            return csv_parser.parse(file_path)
        case SupportedInput.JSON.value:
            return json_parser.parse(file_path)
        case SupportedInput.YAML.value:
            return yaml_parser.parse(file_path)
        case _:
            raise ValueError(f"Unsupported file extension {file_extension}.")
