from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class UserNotification(BaseModel):
    user_id: Optional[str] = None
    id: Optional[str] = None
    status: Optional[str] = None
    departure_delay: Optional[float] = None
    arrival_delay: Optional[float] = None
    scheduled_off: Optional[datetime] = None
    scheduled_out: Optional[datetime] = None
    estimated_out: Optional[datetime] = None
    actual_out: Optional[datetime] = None
    estimated_off: Optional[datetime] = None
    actual_off: Optional[datetime] = None
    scheduled_on: Optional[datetime] = None
    estimated_on: Optional[datetime] = None
    actual_on: Optional[datetime] = None
    scheduled_in: Optional[datetime] = None
    estimated_in: Optional[datetime] = None
    actual_in: Optional[datetime] = None
    foresight_predictions_available: Optional[bool] = None
    created_at: Optional[datetime] = None  # Added this line
    flight_name:Optional[str]=None
    buffer_1:Optional[str]=None
    buffer_2:Optional[str]=None
