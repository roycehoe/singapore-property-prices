import requests

from constants import (
    BASE_URL,
    HDB_RESALE_BY_BUILDING_BLOCK_PATH,
    PRIVATE_PROPERTY_RESALE_BY_LAT_LON_PATH,
    TOKEN,
)


def _deduplicate_resale_data(func):  # resale data returned from API contains duplicates
    def wrapper(*args, **kwargs):
        resale_data = func(*args, **kwargs)
        return [
            dict(deduplicated_data)
            for deduplicated_data in {tuple(data.items()) for data in resale_data}
        ]

    return wrapper


def _get_resale_data_baseURL(property_type: str):
    if property_type == "hdb":
        return f"{BASE_URL}/{HDB_RESALE_BY_BUILDING_BLOCK_PATH}"
    return f"{BASE_URL}/{PRIVATE_PROPERTY_RESALE_BY_LAT_LON_PATH}"


def _get_resale_url(property_data):
    baseURL = _get_resale_data_baseURL(property_data["type"])
    latitude = property_data["latitude"]
    longitude = property_data["longitude"]

    if block := property_data.get("block"):
        return f"{baseURL}?block={block}&latitude={latitude}&longitude={longitude}&token={TOKEN}"
    return f"{baseURL}?block={block}latitude={latitude}&longitude={longitude}&token={TOKEN}"


@_deduplicate_resale_data
def get_resale_data(block_data: dict):
    api_url = _get_resale_url(block_data)
    response = requests.get(api_url).json()
    return response
