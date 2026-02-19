from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.users.schemas import UserCreate
from app.users.repository import UserRepository
from app.users.models import User
from typing import List


class UserService:

    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, user_in: UserCreate) -> User:
        try:
            return self.repo.create(
                username=user_in.username,
                email=user_in.email
            )
        except IntegrityError:
            raise ValueError("Username or Email already exists")

    def list_users(self) -> List[User]:
        return self.repo.list()
