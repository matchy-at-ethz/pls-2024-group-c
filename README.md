# `gillespie`: Python Gillespie Algorithm Simulation

This is an implementation of the Gillespie Algorithm in Python. The package by
default performs simulation of the following reaction system:

## Installation

Navigate to the root directory of this project, install the dependencies and
then install this package

```bash
cd /<project-root>
pip install -r requirements.txt
pip install .
```

For development purpose, one can install it as an editable package via `pip
install -e .`

### Additional dependencies for GUI

On **Linux** systems, the following additional dependencies are required to run the
GUI (example for Ubuntu/Debian):

```bash
sudo apt install libxcb-xinerama0
sudo apt install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
```

## Use the package

### Command Line Interface (CLI)

After installing it as an editable package, one can simply run the simulation
via running the `gillepsie` command:

```bash
gillepsie
```

### Graphical User Interface (GUI)

```bash
gillepsie-gui
```
