from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.users.schemas import UserCreate, UserRead, UserList
from app.users.services import UserService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserRead, status_code=201)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        return service.create_user(user_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=UserList)
def list_users(db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        users = service.list_users()
        return {"users": users}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
