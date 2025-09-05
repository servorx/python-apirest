from app.models.reservation.ReservationModel import Reservation
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date, time

class Room(SQLModel, table=True):
    __tablename__ = "rooms"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False)
    sede: str = Field(max_length=50, nullable=False)
    capacidad: int = Field(nullable=False)
    recursos: str = Field(max_length=50, nullable=False)

    # Relación uno-a-muchos con reservas
    reservations: List["Reservation"] = Relationship(
        back_populates="sala",
        passive_deletes=True  
    )