import enum

from datetime import datetime, timezone
from db.connection import Base
from sqlalchemy import Column, Integer, String, Enum, Float, DateTime


class HardwareResources(Base):
    __tablename__ = "hardwareResources"
    id = Column(Integer, primary_key=True, index=True)
