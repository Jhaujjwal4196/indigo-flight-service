from app.models.flights import FlightUpdate
from app.models.userTable import User
from app.models.userNotificationTable import UserNotificationTable
from app.models.flightUserTable import FlightUserTable
from sqlalchemy.orm import Session
import json
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from datetime import datetime
import uuid  # Import uuid for generating unique IDs

def notify_user(flight_status: FlightUpdate, db: Session):
    try:
        all_users = db.query(FlightUserTable).filter(FlightUserTable.flight_id == flight_status.id).all()
        
        for user_entry in all_users:
            print(user_entry.user_id, "users")
            
            curr_user = db.query(User).filter(User.id == user_entry.user_id).first()
            
            if curr_user:
                flight_status_dict = flight_status.dict()
                
                notification_entry = UserNotificationTable(
                    user_id=curr_user.id,
                    id=flight_status.id,  
                    status=flight_status.status,
                    departure_delay=flight_status.departure_delay,
                    arrival_delay=flight_status.arrival_delay,
                    scheduled_off=flight_status.scheduled_off,
                    scheduled_out=flight_status.scheduled_out,
                    estimated_out=flight_status.estimated_out,
                    actual_out=flight_status.actual_out,
                    estimated_off=flight_status.estimated_off,
                    actual_off=flight_status.actual_off,
                    scheduled_on=flight_status.scheduled_on,
                    estimated_on=flight_status.estimated_on,
                    actual_on=flight_status.actual_on,
                    scheduled_in=flight_status.scheduled_in,
                    estimated_in=flight_status.estimated_in,
                    actual_in=flight_status.actual_in,
                    foresight_predictions_available=flight_status.foresight_predictions_available,
                    created_at=datetime.utcnow()  # Current UTC time
                )
                db.add(notification_entry)
                
                # Update user notifications
                if curr_user.notifications is None:
                    curr_user.notifications = []
                curr_user.notifications.append(flight_status_dict)

                print()
                print(curr_user.notifications)
                print()
                
                try:
                    db.commit()
                    db.refresh(curr_user)
                except Exception as e:
                    print(f"Error committing changes: {e}")
                    db.rollback()  # Rollback if committing fails
            else:
                print(f"User with ID {user_entry.user_id} not found.")
    
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="An error occurred while processing notifications.")

    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
