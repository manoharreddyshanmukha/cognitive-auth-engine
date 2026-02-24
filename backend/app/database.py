from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = os.getenv("postgresql://cognitive_auth_db_user:ypDWxA6hib9F9geQWd7OUIbMdgAYrMJa@dpg-d6ev7pp5pdvs73f39h5g-a/cognitive_auth_db")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()