from sqlalchemy.orm import Session
from app.models.flight import Flight as FlightModel
from app.models.schemas import FlightUpdate, FlightSearch
from sqlalchemy.exc import SQLAlchemyError
from fastapi import  HTTPException
from datetime import datetime, timezone, timedelta
from sqlalchemy import and_, cast, String, func
import time

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


def filter_flights(filter_data: FlightSearch, db: Session):
    query = db.query(FlightModel)

    if filter_data.id:
        query = query.filter(FlightModel.id == filter_data.id)
        return query.all()

    if filter_data.pnr:
        query = query.filter(FlightModel.pnr == filter_data.pnr)
        return query.all()

    if filter_data.date:
        filter_date = datetime.strptime(filter_data.date, "%Y-%m-%d")
        next_day = filter_date + timedelta(days=1)
    else:
        filter_date = None
        next_day = None

    if filter_data.arrival and filter_data.departure and filter_data.date:
        query = query.filter(
            and_(
                FlightModel.origin_city.contains(f"{filter_data.arrival}"),
                FlightModel.destination_city.contains(f"{filter_data.departure}"),
                FlightModel.scheduled_out >= filter_date,
                FlightModel.scheduled_out < next_day
            )
        )
        return query.all()

    # If none of the conditions matched, return an empty list
    return []


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

        if new_value and (new_value != old_value or True):
            setattr(flight, field, new_value)
            fields_to_update[field] = new_value

    if fields_to_update:
        db.commit()
        db.refresh(flight)

        # Include flight ID and flight name in the message body
        serialized_data = serialize_datetimes(fields_to_update)
        serialized_data['id'] = flight_id
        serialized_data['flight_name'] = flight.ident_iata

        # Retry mechanism for RabbitMQ connection
        max_retries = 5
        for attempt in range(max_retries):
            try:
                connection_params = pika.ConnectionParameters(
                    host='localhost',
                    heartbeat=600,
                    blocked_connection_timeout=300
                )
                connection = pika.BlockingConnection(connection_params)
                channel = connection.channel()

                channel.basic_publish(
                    exchange='',
                    routing_key='flight_updates',
                    body=json.dumps(serialized_data)
                )
                connection.close()
                break  # Exit the loop if publish is successful
            except pika.exceptions.AMQPConnectionError as e:
                print(f"Connection error: {e}. Retrying {attempt + 1}/{max_retries}")
                time.sleep(2 ** attempt)  # Exponential backoff
            except Exception as e:
                print(f"Unexpected error: {e}")
                break

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

    # except Exception as e:
    #     print(f"Unexpected error: {e}")
    #     raise HTTPException(status_code=500, detail="An unexpected error occurred.")