from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models.flightUserSchema import FlightUserSchema
from app.services.booking_service import create_booking, get_bookings
from app.db.database import get_db
from typing import List

router = APIRouter()

@router.post('/bookings', response_model=FlightUserSchema)
async def create_flight_booking(flight_booking : FlightUserSchema, db: Session = Depends(get_db)):
    try:
        book_flight = create_booking(flight_booking,db)
        return book_flight
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@router.get('/bookings', response_model=List[FlightUserSchema])
async def get_all_bookings(db: Session = Depends(get_db)):
    try:
        book_flight = get_bookings(db)
        return book_flight
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")



