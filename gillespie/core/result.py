from dataclasses import dataclass
from typing import Union, Dict
import numpy as np


@dataclass
class Result:
    time: np.ndarray[Union[int, float]]
    species: Dict[str, np.ndarray[Union[int, float]]]
