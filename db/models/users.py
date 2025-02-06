import enum

from datetime import datetime, timezone
from db.connection import Base
from sqlalchemy import Column, Integer, String, Enum, Float, DateTime


class UserTypes(enum.Enum):
    client = 0
    host = 1
    both = 2


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    type = Column(Enum(UserTypes), nullable=True)
    balance = Column(Float, default=0.0)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
