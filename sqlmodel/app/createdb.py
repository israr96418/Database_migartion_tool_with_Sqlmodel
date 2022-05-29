from sqlmodel import SQLModel

from app.database import engine
import app.models


def create_db_table():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_table()