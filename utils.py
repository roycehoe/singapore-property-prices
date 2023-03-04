import json
from typing import Any


def write_to_database(path: str, data: Any) -> None:
    with open(path, "+r") as f:
        file_data = json.load(f)
        file_data.append(data)
