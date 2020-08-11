import os
from typing import Optional

from fastapi import FastAPI, status, Response, Depends
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy.orm import Session

from db import SessionLocal, engine
import crud, models


class User(BaseModel):
    id: Optional[int]
    username: Optional[str] = Field(None, max_length=256)
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

    class Config:
        orm_mode = True


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def hello():
    return 'Hello world from ' + os.environ['HOSTNAME'] + ' !'


@app.get("/health/")
async def health():
    return {"status": "OK"}


@app.post("/user/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User, db: Session = Depends(get_db)):
    db_user=models.User(username=user.username, firstname=user.firstName, lastname=user.lastName, email=user.email, phone=user.phone)
    crud.create_user(db=db, user=db_user)
    user.id=db_user.id
    return user.dict()


@app.get("/user/{userId}", response_model=User)
async def get_user(userId: int, response: Response, db: Session = Depends(get_db)):
    db_user=crud.get_user(db, userId)
    if db_user is None:
        response.status_code=status.HTTP_404_NOT_FOUND
        return None
    user = User(id=db_user.id, username=db_user.username, firstName=db_user.firstname, lastName=db_user.lastname, email=db_user.email, phone=db_user.phone)
    return user.dict()


@app.delete("/user/{userId}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(userId: int, response: Response, db: Session = Depends(get_db)):
    db_user=crud.delete_user(db, userId)
    if db_user is None:
        response.status_code=status.HTTP_404_NOT_FOUND
    return None


@app.put("/user/{userId}")
async def update_user(userId: int, user: User, response: Response, db: Session = Depends(get_db)):
    db_user=models.User(id=userId, username=user.username, firstname=user.firstName, lastname=user.lastName, email=user.email, phone=user.phone)
    db_user=crud.update_user(db, db_user)
    if db_user is None:
        response.status_code=status.HTTP_404_NOT_FOUND
        return None
    user = User(id=db_user.id, username=db_user.username, firstName=db_user.firstname, lastName=db_user.lastname, email=db_user.email, phone=db_user.phone)
    return user.dict()
