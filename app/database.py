import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_database_url = os.environ.get('DATABASE_URL')
print(sqlalchemy_database_url)
engine = create_engine(sqlalchemy_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
