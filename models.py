from sqlalchemy import Column, Integer, String

from database import Base


class PropertyLocation(Base):
    __tablename__ = "property_location"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    block = Column(String)
    street_name = Column(String)
    address = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    type = Column(String)
