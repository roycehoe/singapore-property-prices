from dataclasses import dataclass
from database import SessionLocal
from schemas.crud import DatabaseCRUD
from dataclasses import dataclass
from sqlalchemy.orm import Session

from schemas.resale_location import ResaleLocationData
from models import PropertyLocation


@dataclass
class ResaleLocationDB(DatabaseCRUD):
    db: Session = SessionLocal()

    def get(self, id):
        raise NotImplementedError

    def get_all(self):
        with self.db as session:
            return session.query(PropertyLocation).all()

    def create(self, new_row: ResaleLocationData) -> ResaleLocationData:
        raise NotImplementedError

    def create_many(
        self, new_rows: list[ResaleLocationData]
    ) -> list[ResaleLocationData]:
        with self.db as session:
            session.add_all(new_rows)
            session.commit()
            return new_rows

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
