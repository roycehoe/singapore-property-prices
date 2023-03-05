from schemas.resale_location import ResaleLocationData
from scripts.get_resale_location_data import (
    get_resale_location_data,
    init_resale_location_data,
)

import models
from database import engine

models.Base.metadata.create_all(bind=engine)

init_resale_location_data()
data = get_resale_location_data()
