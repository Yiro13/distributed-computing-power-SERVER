import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv("DATABASEURL"))
Session = sessionmaker(bind=engine)

Base = declarative_base()
