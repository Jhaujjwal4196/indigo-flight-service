from pydantic import BaseModel

class FlightUserSchema(BaseModel):
    user_id: str
    flight_id: str