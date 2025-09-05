from fastapi import FastAPI
from app.core.database import create_db_and_tables
from app.auth.auth import auth
from app.models.room.RoomModel import Room
from app.models.reservation.ReservationModel import Reservation
from app.routes import RoomsRoutes, ReservationRoutes, UserRoutes
app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()



@app.get("/")
def root():
    return {"Esto funciona milagrosamente"}

app.include_router(auth)
app.include_router(UserRoutes.router)
app.include_router(RoomsRoutes.router)
app.include_router(ReservationRoutes.router)
