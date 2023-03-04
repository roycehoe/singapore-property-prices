from pydantic import BaseModel


class ResaleLocationData(BaseModel):
    description: str
    block: str
    street_name: str
    address: str
    latitude: str
    longitude: str
    type: str

    class Config:
        orm_mode = True
