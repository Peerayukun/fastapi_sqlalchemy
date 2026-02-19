from sqlalchemy import Column, Integer, String
from app.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(10), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
