from dataclasses import dataclass
from typing import Any
from database import SessionLocal
from dataclasses import dataclass
from sqlalchemy.orm import Session


@dataclass
class SqliteDB:
    db: Session = SessionLocal()

    def get(self):
        raise NotImplementedError

    def get_all(self, table: Any) -> list[Any]:
        with self.db as session:
            return session.query(table).all()

    def create(self):
        raise NotImplementedError

    def create_many(self, new_rows: list[Any]) -> list[Any]:
        with self.db as session:
            session.add_all(new_rows)
            session.commit()
            return new_rows

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
