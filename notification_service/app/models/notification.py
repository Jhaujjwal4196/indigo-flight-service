from pydantic import BaseModel

class FlightStatus(BaseModel):
    id: int
    name: str
    status: str
