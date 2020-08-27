import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_host = os.environ.get('DATABASE_HOST', '')
db_port = os.environ.get('DATABASE_PORT', '')
db_name = os.environ.get('DATABASE_NAME', '')
db_user = os.environ.get('DATABASE_USER', '')
db_password = os.environ.get('DATABASE_PASSWORD', '')


SQLALCHEMY_DATABASE_URL = "postgresql://"+db_user+":"+db_password+"@"+db_host+":"+str(db_port)+"/"+db_name

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
