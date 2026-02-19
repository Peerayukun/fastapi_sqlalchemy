from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
from app.users.models import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, username: str, email: str) -> User:
        user = User(username=username, email=email)
        self.db.add(user)
        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise
        self.db.refresh(user)
        return user

    def list(self) -> List[User]:
        return self.db.query(User).order_by(User.id).all()
