from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import TypeDecorator, TEXT

Base = declarative_base()

class JSONType(TypeDecorator):
    impl = TEXT

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return str(value)  # Serialize complex types to string

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return eval(value)  # Deserialize strings to complex types

class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True, index=True)
    ident = Column(String, nullable=True)
    ident_icao = Column(String, nullable=True)
    ident_iata = Column(String, nullable=True)
    actual_runway_off = Column(String, nullable=True)
    actual_runway_on = Column(String, nullable=True)
    fa_flight_id = Column(String, nullable=True)
    operator = Column(String, nullable=True)
    operator_icao = Column(String, nullable=True)
    operator_iata = Column(String, nullable=True)
    flight_number = Column(String, nullable=True)
    registration = Column(String, nullable=True)
    atc_ident = Column(String, nullable=True)
    inbound_fa_flight_id = Column(String, nullable=True)
    codeshares = Column(JSONType, nullable=True)  # Use JSONType for lists
    codeshares_iata = Column(JSONType, nullable=True)
    blocked = Column(Boolean, nullable=True)
    diverted = Column(Boolean, nullable=True)
    cancelled = Column(Boolean, nullable=True)
    position_only = Column(Boolean, nullable=True)
    origin = Column(JSONType, nullable=True)  # Use JSONType for complex objects
    destination = Column(JSONType, nullable=True)
    departure_delay = Column(Float, nullable=True)
    arrival_delay = Column(Float, nullable=True)
    filed_ete = Column(Float, nullable=True)
    progress_percent = Column(Float, nullable=True)
    status = Column(String, nullable=True)
    aircraft_type = Column(String, nullable=True)
    route_distance = Column(Float, nullable=True)
    filed_airspeed = Column(Float, nullable=True)
    filed_altitude = Column(Float, nullable=True)
    route = Column(String, nullable=True)
    baggage_claim = Column(String, nullable=True)
    seats_cabin_business = Column(Integer, nullable=True)
    seats_cabin_coach = Column(Integer, nullable=True)
    seats_cabin_first = Column(Integer, nullable=True)
    gate_origin = Column(String, nullable=True)
    gate_destination = Column(String, nullable=True)
    terminal_origin = Column(String, nullable=True)
    terminal_destination = Column(String, nullable=True)
    type = Column(String, nullable=True)
    scheduled_out = Column(DateTime, nullable=True)
    estimated_out = Column(DateTime, nullable=True)
    actual_out = Column(DateTime, nullable=True)
    scheduled_off = Column(DateTime, nullable=True)
    estimated_off = Column(DateTime, nullable=True)
    actual_off = Column(DateTime, nullable=True)
    scheduled_on = Column(DateTime, nullable=True)
    estimated_on = Column(DateTime, nullable=True)
    actual_on = Column(DateTime, nullable=True)
    scheduled_in = Column(DateTime, nullable=True)
    estimated_in = Column(DateTime, nullable=True)
    actual_in = Column(DateTime, nullable=True)
    foresight_predictions_available = Column(Boolean, nullable=True)
