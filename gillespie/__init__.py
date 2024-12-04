from pathlib import Path
from importlib.metadata import metadata, PackageNotFoundError, version


def get_package_root() -> Path:
    """Get the root directory of the package."""
    return Path(__file__).parent


def get_metadata() -> dict:
    """Get the metadata of the package."""
    try:
        return metadata("gillespie")
    except PackageNotFoundError:
        # If package is not installed, read from pyproject.toml
        try:
            import tomli
        except ImportError:
            import tomllib as tomli
        pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
        with open(pyproject_path, "rb") as f:
            pyproject_data = tomli.load(f)
        return pyproject_data["project"]


META = get_metadata()


def get_package_name() -> str:
    """Get the name of the package."""
    return META["name"]


def get_version():
    """Get version from installed package or pyproject.toml."""
    try:
        # Try getting version from installed package first
        return version("gillespie")
    except PackageNotFoundError:
        # If package is not installed, read from pyproject.toml
        try:
            import tomli
        except ImportError:
            import tomllib as tomli  # Python 3.11+ has tomllib in stdlib

        pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
        try:
            with open(pyproject_path, "rb") as f:
                pyproject_data = tomli.load(f)
            return pyproject_data["project"]["version"]
        except (FileNotFoundError, KeyError, tomli.TOMLDecodeError):
            return "unknown"


__version__ = get_version()
__package__ = get_package_name()

from .gui import launch_gui
from .core import Simulation

__all__ = ["launch_gui", "Simulation"]
