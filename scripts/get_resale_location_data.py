from typing import Callable
import requests

from constants import (
    BASE_URL,
    RESALE_LOCATION_DATA_PATH,
    RESALE_LOCATION_DEFAULT_PARAMS,
    RESALE_LOCATION_PATH,
    TOKEN,
    TOTAL_DISTRICTS,
)
from utils import write_to_database


def _log_district_scrapped_from_website(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"district scraped: {args[0]}")
        return result

    return wrapper


@_log_district_scrapped_from_website
def _get_resale_location_datapoint(district: int) -> list[dict]:
    response = requests.get(
        f"{BASE_URL}/{RESALE_LOCATION_PATH}{RESALE_LOCATION_DEFAULT_PARAMS}&district={district}&token={TOKEN}"
    )
    return response.json()


def init_resale_location_data(total_districts: int = TOTAL_DISTRICTS) -> None:
    for i in range(1, total_districts):
        write_to_database(RESALE_LOCATION_DATA_PATH, _get_resale_location_datapoint(i))
