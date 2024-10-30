"""Package metadata and setup information. I stole this from the demo one"""

from pathlib import Path
from setuptools import setup, find_packages
import sys
import os

ROOT_DIR: Path = Path(__file__).parent.resolve()

exec(open(ROOT_DIR / "Projectconfiguration.py", encoding="utf-8").read())

with open(ROOT_DIR / "requirements.txt", "r", encoding="utf-8") as _file: #currently empty, tk inter should probably be added
    INSTALL_REQUIRES = _file.read().splitlines()

setup(
    name="gillespie",
    version=VERSION,  # noqa: F821 # the yellow underline is fine
    packages=find_packages(),
    entry_points={
        "console_scripts": ["gillespie-gui=Main.GUI.App:main",
        "gillespie-simulate= Main.App:main"],
    },
    install_requires=INSTALL_REQUIRES,
)
