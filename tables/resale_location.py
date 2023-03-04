from dataclasses import dataclass
from database import get_db
from schemas.crud import DatabaseCRUD
from dataclasses import dataclass
from sqlalchemy.orm import Session
from typing import Generator

from schemas.resale_location import ResaleLocationData


@dataclass
class ResaleLocationDB(DatabaseCRUD):
    db: Session = get_db()

    def get(self, id):
        raise NotImplementedError

    def get_all(self):
        return self.db.query(ResaleLocationData).all()

    def create(self, new_row: ResaleLocationData) -> ResaleLocationData:
        self.db.add(new_row)
        self.db.commit()
        self.db.refresh(new_row)
        return new_row

    def create_many(
        self, new_rows: list[ResaleLocationData]
    ) -> list[ResaleLocationData]:
        self.db.add_all(new_rows)
        self.db.commit()
        self.db.refresh(new_rows)
        return new_rows

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
