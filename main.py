import requests
import json

TOTAL_DISTRICTS = 28
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMsInVzZXJfaWQiOjMsImVtYWlsIjoicHVibGljQXBpUm9sZUBzbGEuZ292LnNnIiwiZm9yZXZlciI6ZmFsc2UsImlzcyI6Imh0dHA6XC9cL29tMi5kZmUub25lbWFwLnNnXC9hcGlcL3YyXC91c2VyXC9zZXNzaW9uIiwiaWF0IjoxNjc3OTAyMDgyLCJleHAiOjE2NzgzMzQwODIsIm5iZiI6MTY3NzkwMjA4MiwianRpIjoiNmI5NDFhZGRiNTg2N2M3NGQ5NGQxZTIwODFmZjc5MWMifQ.gE2yjDlRWuzK1y8aCUTnRMa8b5djMoh2DkyJBHtfUC0"

BASE_URL = "https://developers.onemap.sg/publicapi/propsvc"
RESALE_BLOCK_PATH = "retrieve_property_locations_within_district"
HDB_RESALE_BY_BUILDING_BLOCK_PATH= "getHDBResaleByBuildingBlock"
PPT_RESALE_BY_LAT_LON_PATH= "getHDBResaleByBuildingBlock"

RESALE_BLOCK_DEFAULT_PARAMS = "?apartment=true&condo=true&executive_condo=true&executive_hdb=true&five_room_hdb=true&four_room_hdb=true&landed=true&lower_bound_date=20220304&lower_bound_price=0&multi_gen_hdb=true&one_room_hdb=true&three_room_hdb=true&two_room_hdb=true&upper_bound_date=20230304&upper_bound_price=200000000"

def get_property_API_baseURL(type: str):
    if type == "hdb":
        return f'{BASE_URL}/{HDB_RESALE_BY_BUILDING_BLOCK_PATH}'
    return f'{BASE_URL}/{PPT_RESALE_BY_LAT_LON_PATH}'

def get_property_API_url(property_data):
    baseURL = get_property_API_baseURL(property_data["type"])
    latitude = property_data["latitude"]
    longitude = property_data["longitude"]

    if (block := property_data.get("block")):
        return f"{baseURL}?block={block}&latitude={latitude}&longitude={longitude}&token={TOKEN}"
    return f"{baseURL}?block={block}latitude={latitude}&longitude={longitude}&token={TOKEN}"

def get_resale_block_data(district: int):
    response = requests.get(f"{BASE_URL}/{RESALE_BLOCK_PATH}{RESALE_BLOCK_DEFAULT_PARAMS}&district={district}&token={TOKEN}")
    return response.json()

def _init_resale_block_data(total_districts=TOTAL_DISTRICTS):
    resale_block_data = []
    for i in range(1, total_districts):
        resale_block_data = [*resale_block_data, *get_resale_block_data(i)]
        print("done with district", i)
    with open("resale_block_data.json", "w") as f:
        f.write(json.dumps(resale_block_data))


def get_resale_data(block_data: dict):
    api_url = get_property_API_url(block_data)
    response = requests.get(api_url).json()
    return [dict(t) for t in {tuple(d.items()) for d in response}]

with open("resale_block_data.json", "r") as f:
    block_data = json.load(f)

for i in range(10):
    something = get_resale_data(block_data[i])

print(something)