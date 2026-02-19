from alembic import context
from sqlalchemy import create_engine

from app.db import Base, SQLALCHEMY_DATABASE_URL
from app.users import models  # register models

config = context.config
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

target_metadata = Base.metadata


def run_migrations_online():
    connectable = create_engine(SQLALCHEMY_DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
