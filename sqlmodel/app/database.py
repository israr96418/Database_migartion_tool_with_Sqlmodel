from sqlmodel import create_engine, Session

# DATABASE_NAME = "./order.db"
# DATABASE_URL = f"sqlite:///{DATABASE_NAME}"
sqlite_url = "mysql+mysqldb://isrardawar:dawar96418@localhost:3306/sqlmodel"
engine = create_engine(sqlite_url, echo=True)

SessionLocal = Session(bind=engine)


def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()