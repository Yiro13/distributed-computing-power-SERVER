import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()
engine = create_engine(os.getenv("DATABASEURL"))
SessionLocal = sessionmaker(bind=engine, autoflush=False)
