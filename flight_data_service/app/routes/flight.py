from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.flight import Flight as FlightModel
from app.models.schemas import Flight as FlightSchema, FlightCreate, FlightUpdate, FlightSearch
from app.services.flight_service import get_flight, update_flight_status, create_flight, filter_flights

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/flights/{flight_id}", response_model=FlightSchema)
async def read_flight(flight_id: int, db: Session = Depends(get_db)):
    flight = get_flight(db, flight_id)
    if flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight

@router.get("/flights", response_model=List[FlightSchema])
async def get_flights(
    id: str = Query(None),
    arrival: str = Query(None),
    departure: str = Query(None),
    date: str = Query(None),
    pnr: str = Query(None),
    db: Session = Depends(get_db)
):
    try:
        filter_data = FlightSearch(id=id, arrival=arrival, departure=departure, date=date, pnr=pnr)
        flights = filter_flights(filter_data, db)
        return flights
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.post("/flights/", response_model=FlightSchema)
async def create_flight_endpoint(flight_create: FlightCreate, db: Session = Depends(get_db)):
    flight = create_flight(db, flight_create)
    if flight is None:
        raise HTTPException(status_code=400, detail="Flight creation failed")
    return flight

@router.put("/flights/{flight_id}", response_model=FlightSchema)
async def update_flight(flight_id: str, flight_update: FlightUpdate, db: Session = Depends(get_db)):
    flight = update_flight_status(db, flight_id, flight_update)
    if flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight
