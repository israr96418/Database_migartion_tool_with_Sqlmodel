from fastapi import FastAPI
from sqlmodel import select
from app.database import Session, engine
from app.models import Product

app = FastAPI()

session = Session(bind=engine)


@app.get("/")
def get():
    data = session.exec(select(Product)).all()
    return {"message": data}


@app.post("/", response_model=Product)
def post_data(data: Product):
    store = Product(**data.dict())
    session.add(store)
    session.commit()
    # session.refresh(store)
    return store
