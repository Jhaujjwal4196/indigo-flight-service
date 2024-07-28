from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class FlightUserTable(Base):
    __tablename__ = 'flight_user'

    user_id = Column(String, nullable=False, primary_key=True)
    flight_id = Column(String, nullable=False, primary_key=True)
   

