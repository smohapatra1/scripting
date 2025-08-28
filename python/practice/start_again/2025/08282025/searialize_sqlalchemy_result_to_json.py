#   https://www.geeksforgeeks.org/python/serialize-python-sqlalchemy-result-to-json/

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class User(Base):
    __tablename__ == 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

engine = create_engine('sqlite:///:memory:') 
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

