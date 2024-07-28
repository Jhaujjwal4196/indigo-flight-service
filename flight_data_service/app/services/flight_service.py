from sqlalchemy.orm import Session
from app.models.flight import Flight as FlightModel
from app.models.schemas import FlightUpdate
from sqlalchemy.exc import SQLAlchemyError
import json


from app.models.schemas import FlightCreate


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='flight_updates')


def get_flight(db: Session, flight_id: int):
    return db.query(FlightModel).filter(FlightModel.id == flight_id).first()

def update_flight_status(db: Session, flight_id: int, flight_update: FlightUpdate):
    flight = db.query(FlightModel).filter(FlightModel.id == flight_id).first()
    if flight:
        flight.status = flight_update.status
        flight.actual_in=flight_update.actual_in
        flight.actual_off=flight_update.actual_off
        flight.scheduled_in=flight_update.scheduled_in
        flight.scheduled_off=flight_update.scheduled_off
        flight.scheduled_on=flight_update.scheduled_on
        flight.scheduled_out=flight_update.scheduled_out
        flight.actual_on=flight_update.actual_on
        flight.actual_out=flight_update.actual_out
        flight.estimated_in=flight_update.estimated_in
        flight.estimated_off=flight_update.estimated_off
        flight.estimated_on=flight_update.estimated_on
        flight.estimated_out=flight_update.estimated_out
        db.commit()
        db.refresh(flight)

        channel.basic_publish(
        exchange='',
        routing_key='flight_updates',
        body=json.dumps(flight_update.dict())
    )
        return flight
    return None

def create_flight(db: Session, flight_create: FlightCreate):
    try:
        db_flight = FlightModel(**flight_create.dict())
        print(db_flight)
        db.add(db_flight)
        db.commit()
        db.refresh(db_flight)

        return db_flight
    
    except SQLAlchemyError as e:
        # db.rollback()
        print(f"Error occurred while creating flight: {e}")
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="An error occurred while creating the flight.")

    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")