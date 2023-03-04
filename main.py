import requests
import json

from constants import (
    BASE_URL,
    HDB_RESALE_BY_BUILDING_BLOCK_PATH,
    PPT_RESALE_BY_LAT_LON_PATH,
    RESALE_LOCATION_DEFAULT_PARAMS,
    RESALE_LOCATION_PATH,
    TOKEN,
    TOTAL_DISTRICTS,
)


def get_resale_location_data(district: int):
    response = requests.get(
        f"{BASE_URL}/{RESALE_LOCATION_PATH}{RESALE_LOCATION_DEFAULT_PARAMS}&district={district}&token={TOKEN}"
    )
    return response.json()


def _init_resale_location_data(total_districts=TOTAL_DISTRICTS):
    resale_location_data = []
    for i in range(1, total_districts):
        resale_location_data = [*resale_location_data, *get_resale_location_data(i)]
        print("done with district", i)
    with open("resale_block_data.json", "w") as f:
        f.write(json.dumps(resale_location_data))


def get_resale_data_baseURL(type: str):
    if type == "hdb":
        return f"{BASE_URL}/{HDB_RESALE_BY_BUILDING_BLOCK_PATH}"
    return f"{BASE_URL}/{PPT_RESALE_BY_LAT_LON_PATH}"


def get_resale_url(property_data):
    baseURL = get_resale_data_baseURL(property_data["type"])
    latitude = property_data["latitude"]
    longitude = property_data["longitude"]

    if block := property_data.get("block"):
        return f"{baseURL}?block={block}&latitude={latitude}&longitude={longitude}&token={TOKEN}"
    return f"{baseURL}?block={block}latitude={latitude}&longitude={longitude}&token={TOKEN}"


def get_resale_data(block_data: dict):
    api_url = get_resale_url(block_data)
    response = requests.get(api_url).json()
    return [dict(t) for t in {tuple(d.items()) for d in response}]


with open("resale_block_data.json", "r") as f:
    block_data = json.load(f)

for i in range(10):
    something = get_resale_data(block_data[i])
