from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from nanoid import generate

Base = declarative_base()

def generate_id():
    return generate(size=21)

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, default=generate_id)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    roles = Column(JSON, default=[])
    notifications = Column(JSON, default=[])
    created_at = Column(DateTime, default=datetime.utcnow)
    dob = Column(DateTime, nullable=False)

