from app.models.notification import FlightStatus

users = {
    1: {"email": "user1@example.com", "phone": "+1234567890"},
    2: {"email": "user2@example.com", "phone": "+0987654321"},
}




def notify_user(flight_status: FlightStatus):
    user = users.get(flight_status.id)
    if user:
        # Here, you can integrate with an email/SMS service to send notifications
        print(f"Sending notification to {user['email']} and {user['phone']} about {flight_status.name} status: {flight_status.status}")
        return flight_status
    return None
