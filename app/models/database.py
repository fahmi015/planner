from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config
from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URL = config("database_driver")+"://"+config("database_user")+"@"+config("database_host")+"/"+config("database_name")
if config("database_password"):
    SQLALCHEMY_DATABASE_URL = config("database_driver")+"://"+config("database_user")+":"+config("database_password")+"@"+config("database_host")+"/"+config("database_name")

print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

