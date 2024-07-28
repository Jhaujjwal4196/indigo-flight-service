from sqlalchemy import create_engine
from app.models.userTable import Base  
from app.models.flightUserTable import Base as FlightBase


DATABASE_URL = "sqlite:///./test.db" 
engine = create_engine(DATABASE_URL)
# Base.metadata.create_all(bind=engine)
FlightBase.metadata.create_all(bind=engine)

print("Tables created successfully")
