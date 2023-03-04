from dataclasses import dataclass
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Generator, Protocol


@dataclass
class DatabaseCRUD(Protocol):
    db: Session

    def get(self):
        ...

    def create(self):
        ...

    def update(self):
        ...

    def delete(self):
        ...
