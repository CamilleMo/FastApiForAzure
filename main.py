from typing import List

from fastapi import FastAPI, status, Depends
from sqlalchemy.orm import Session
from src import models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/customers/", response_model=List[schemas.Customers],
         status_code=status.HTTP_200_OK)
def read_customers(skip: int = 0, limit: int = 100,
                   db: Session = Depends(get_db)):
    return db.query(models.Customers).offset(skip).limit(limit).all()
