from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date, time
from app.models.reservation.ReservationModel import Reservation

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False)
    email: str = Field(max_length=50, nullable=False, index=True, unique=True)
    contraseña_hash: str = Field(max_length=255, nullable=False)
    rol: str = Field(max_length=50, nullable=False)

    # Relación uno-a-muchos con reservas
    reservations: list["Reservation"] = Relationship(back_populates="usuario", sa_relationship_kwargs={"cascade": "all, delete"})