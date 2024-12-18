import json
from pathlib import Path
from typing import Any, Dict


# TODO: implement the yaml parser
def parse(file_path: Path) -> Dict[str, Any]:
    return json.load(file_path.open())
