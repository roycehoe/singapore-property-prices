import requests
import json

from constants import (
    BASE_URL,
    HDB_RESALE_BY_BUILDING_BLOCK_PATH,
    PPT_RESALE_BY_LAT_LON_PATH,
    RESALE_LOCATION_DATA_PATH,
    RESALE_LOCATION_DEFAULT_PARAMS,
    RESALE_LOCATION_PATH,
    TOKEN,
    TOTAL_DISTRICTS,
)


def _get_resale_location_datapoint(district: int) -> list[dict]:
    response = requests.get(
        f"{BASE_URL}/{RESALE_LOCATION_PATH}{RESALE_LOCATION_DEFAULT_PARAMS}&district={district}&token={TOKEN}"
    )
    return response.json()


def _get_resale_location_data(total_districts: int = TOTAL_DISTRICTS) -> list[dict]:
    resale_location_data = []
    for i in range(1, total_districts):
        resale_location_data = [
            *resale_location_data,
            *_get_resale_location_datapoint(i),
        ]
    return resale_location_data


def init_resale_location_data(
    total_districts: int = TOTAL_DISTRICTS, database: str = RESALE_LOCATION_DATA_PATH
) -> None:
    resale_location_data = _get_resale_location_data(total_districts)
    with open(database, "w") as f:
        f.write(json.dumps(resale_location_data))
