from sqlalchemy import Column, Integer, String

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    phone = Column(String)
