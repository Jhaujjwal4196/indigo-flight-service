from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

class FlightBase(BaseModel):
    ident: Optional[str] = None
    ident_icao: Optional[str] = None
    ident_iata: Optional[str] = None
    actual_runway_off: Optional[str] = None
    actual_runway_on: Optional[str] = None
    fa_flight_id: Optional[str] = None
    operator: Optional[str] = None
    operator_icao: Optional[str] = None
    operator_iata: Optional[str] = None
    flight_number: Optional[str] = None
    registration: Optional[str] = None
    atc_ident: Optional[str] = None
    inbound_fa_flight_id: Optional[str] = None
    codeshares: Optional[List[str]] = None
    codeshares_iata: Optional[List[str]] = None
    blocked: Optional[bool] = None
    diverted: Optional[bool] = None
    cancelled: Optional[bool] = None
    position_only: Optional[bool] = None

    origin_code: Optional[str] = None
    origin_code_icao: Optional[str] = None
    origin_code_iata: Optional[str] = None
    origin_code_lid: Optional[str] = None
    origin_timezone: Optional[str] = None
    origin_name: Optional[str] = None
    origin_city: Optional[str] = None
    origin_airport_info_url: Optional[str] = None

    destination_code: Optional[str] = None
    destination_code_icao: Optional[str] = None
    destination_code_iata: Optional[str] = None
    destination_code_lid: Optional[str] = None
    destination_timezone: Optional[str] = None
    destination_name: Optional[str] = None
    destination_city: Optional[str] = None
    destination_airport_info_url: Optional[str] = None

    departure_delay: Optional[float] = None
    arrival_delay: Optional[float] = None
    filed_ete: Optional[float] = None
    progress_percent: Optional[float] = None
    status: Optional[str] = None
    aircraft_type: Optional[str] = None
    route_distance: Optional[float] = None
    filed_airspeed: Optional[float] = None
    filed_altitude: Optional[float] = None
    route: Optional[str] = None
    baggage_claim: Optional[str] = None
    seats_cabin_business: Optional[int] = None
    seats_cabin_coach: Optional[int] = None
    seats_cabin_first: Optional[int] = None
    gate_origin: Optional[str] = None
    gate_destination: Optional[str] = None
    terminal_origin: Optional[str] = None
    terminal_destination: Optional[str] = None
    type: Optional[str] = None
    scheduled_out: Optional[datetime] = None
    estimated_out: Optional[datetime] = None
    actual_out: Optional[datetime] = None
    scheduled_off: Optional[datetime] = None
    estimated_off: Optional[datetime] = None
    actual_off: Optional[datetime] = None
    scheduled_on: Optional[datetime] = None
    estimated_on: Optional[datetime] = None
    actual_on: Optional[datetime] = None
    scheduled_in: Optional[datetime] = None
    estimated_in: Optional[datetime] = None
    actual_in: Optional[datetime] = None
    foresight_predictions_available: Optional[bool] = None

class FlightCreate(FlightBase):
    pass

class FlightUpdate(BaseModel):
    status: Optional[str] = None
    departure_delay: Optional[float] = None
    arrival_delay: Optional[float] = None
    scheduled_off:Optional[datetime]=None
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

    def dict(self, *args, **kwargs):
        data = super().dict(*args, **kwargs)
        # Convert datetime fields to ISO format strings
        for field in ['scheduled_out', 'estimated_out', 'actual_out', 'scheduled_off', 'estimated_off', 'actual_off', 'scheduled_on', 'estimated_on', 'actual_on', 'scheduled_in', 'estimated_in', 'actual_in']:
            if field in data and isinstance(data[field], datetime):
                data[field] = data[field].isoformat()
        return data

    # Add other fields as needed for update operations

class FlightSearch(BaseModel):
    id: Optional[int]=None
    arrival: Optional[str]=None
    departure: Optional[str]=None
    date: Optional[str]=None
    pnr: Optional[str]=None

class Flight(FlightBase):
    id: Optional[int] = None

    
    class Config:
        orm_mode = True
