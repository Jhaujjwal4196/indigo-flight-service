from sqlalchemy.orm import Session
from app.models.flight import Flight as FlightModel
from app.models.schemas import FlightUpdate
from sqlalchemy.exc import SQLAlchemyError
from fastapi import  HTTPException
from datetime import datetime, timezone
import json


from app.models.schemas import FlightCreate


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='flight_updates')


def serialize_datetimes(data):
    for key, value in data.items():
        if isinstance(value, datetime):
            data[key] = value.isoformat()
    return data


def get_flight(db: Session, flight_id: int):
    return db.query(FlightModel).filter(FlightModel.id == flight_id).first()


def update_flight_status(db: Session, flight_id: str, flight_update: FlightUpdate):
    flight = db.query(FlightModel).filter(FlightModel.id == flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")

    fields_to_check = [
        'status', 'actual_in', 'actual_off', 'scheduled_in', 'scheduled_off', 
        'scheduled_on', 'scheduled_out', 'actual_on', 'actual_out', 
        'estimated_in', 'estimated_off', 'estimated_on', 'estimated_out', 'departure_delay', 'arrival_delay'
    ]

    fields_to_update = {}

    for field in fields_to_check:
        new_value = getattr(flight_update, field, None)
        old_value = getattr(flight, field, None)

        if new_value and isinstance(new_value, datetime):
            new_value = new_value.astimezone(timezone.utc).replace(tzinfo=None)

        if new_value and new_value != old_value:
            setattr(flight, field, new_value)
            fields_to_update[field] = new_value

    if fields_to_update:
        db.commit()
        db.refresh(flight)


        # Include flight ID in the message body
        flight_update_dict = flight_update.dict()
        flight_update_dict['id'] = flight_id


        serialized_data = serialize_datetimes(fields_to_update)
        serialized_data['id']=flight_id

        print(serialized_data, "serialized")

        channel.basic_publish(
            exchange='',
            routing_key='flight_updates',
            body=json.dumps(serialized_data)
        )

    return flight

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