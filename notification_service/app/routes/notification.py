from fastapi import APIRouter, HTTPException
from app.models.notification import FlightStatus
from app.services.notification_service import notify_user

router = APIRouter()

@router.post("/notify", response_model=FlightStatus)
async def notify(flight_status: FlightStatus):
    notification = notify_user(flight_status)
    if notification:
        return notification
    raise HTTPException(status_code=404, detail="User not found")
