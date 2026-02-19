from pydantic import BaseModel, EmailStr
from typing import List


class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True  

class UserList(BaseModel):
    users: List[UserRead]
