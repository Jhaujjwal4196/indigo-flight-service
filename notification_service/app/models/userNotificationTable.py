from sqlalchemy import Column, String, Float, DateTime, Boolean, ForeignKey, UniqueConstraint, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class UserNotificationTable(Base):
    __tablename__ = 'user_notifications'
    
    user_id = Column(String, nullable=False)  # User receiving the notification
    id = Column(String, nullable=False)  # This is no longer a primary key
    status = Column(String, nullable=True)
    departure_delay = Column(Float, nullable=True)
    arrival_delay = Column(Float, nullable=True)
    scheduled_off = Column(DateTime(timezone=True), nullable=True)
    scheduled_out = Column(DateTime(timezone=True), nullable=True)
    estimated_out = Column(DateTime(timezone=True), nullable=True)
    actual_out = Column(DateTime(timezone=True), nullable=True)
    estimated_off = Column(DateTime(timezone=True), nullable=True)
    actual_off = Column(DateTime(timezone=True), nullable=True)
    scheduled_on = Column(DateTime(timezone=True), nullable=True)
    estimated_on = Column(DateTime(timezone=True), nullable=True)
    actual_on = Column(DateTime(timezone=True), nullable=True)
    scheduled_in = Column(DateTime(timezone=True), nullable=True)
    estimated_in = Column(DateTime(timezone=True), nullable=True)
    actual_in = Column(DateTime(timezone=True), nullable=True)
    foresight_predictions_available = Column(Boolean, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    _id = Column(Integer, primary_key=True, autoincrement=True)
