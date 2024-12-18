from dataclasses import dataclass
from typing import Union, Dict
import numpy as np


@dataclass
class Result:
    """
    Data class to store the results of a simulation.

    Attributes:
    - time: Array of time points.
    - species: Dictionary of species arrays.
    """

    time: np.ndarray[Union[int, float]]
    species: Dict[str, np.ndarray[Union[int, float]]]
