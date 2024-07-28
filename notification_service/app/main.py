from fastapi import FastAPI
from app.routes import notification
from app.models.flights import FlightUpdate
from app.routes import user

import pika
import json
import threading

app = FastAPI()

# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management

def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='flight_updates')

    def callback(ch, method, properties, body):
        flight_update = FlightUpdate(**json.loads(body))
        print(f"Received notification: {flight_update}")

    channel.basic_consume(
        queue='flight_updates',
        on_message_callback=callback,
        auto_ack=True
    )
    channel.start_consuming()

threading.Thread(target=consume_messages, daemon=True).start()

@app.get("/")
def read_root():
    return {"message": "Notification service is running"}


app.include_router(user.router, prefix="/api")


app.include_router(notification.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)