from fastapi import FastAPI
from app.controllers import create_db_and_tables
from app.auth.auth import auth
from app.models.room.RoomModel import Room
from app.models.reservation.ReservationModel import Reservation
from app.routes import rooms, reservations
app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    # TODO: OBVIAMENTE TENGO QUE REVISAR ESTO
    return {"Esto funciona milagrosamente "}

app.include_router(auth.router)
app.include_router(rooms.router)
app.include_router(reservations.router)
