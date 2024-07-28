from fastapi import FastAPI
from app.db.database import init_db
from app.routes import flight

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    init_db()

app.include_router(flight.router, prefix="/api")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
