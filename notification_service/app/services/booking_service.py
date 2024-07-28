from sqlalchemy.orm import Session
from app.models.flightUserSchema import FlightUserSchema
from app.models.flightUserTable import FlightUserTable
from app.models.userTable import User
from fastapi import  HTTPException
from sqlalchemy.exc import SQLAlchemyError



def create_booking(flight_booking: FlightUserSchema, db:Session):
    try:

        print("flight_booking")
        db_user = db.query(User).filter(User.id == flight_booking.user_id).first()
        print(db_user)
        if not db_user:
            raise HTTPException(status_code=400, detail="Invalid User")

        new_booking = FlightUserTable(
            user_id = flight_booking.user_id,
            flight_id = flight_booking.flight_id
        )
        db.add(new_booking)
        db.commit()  # Commit the transaction
        db.refresh(new_booking)  # Refresh the instance to get the updated data
        return new_booking
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="An error occurred while creating the user.")

def get_bookings(db:Session):
    try:
        all_bookings = db.query(FlightUserTable).all()
        print(all_bookings)
        return all_bookings
    except Exception as e:
         raise HTTPException(status_code=500, detail="An unexpected error occurred.")
