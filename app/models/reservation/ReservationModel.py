from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date, time
from app.models.user.UsersModel import User
from app.models.room.RoomModel import Room

class Reservation(SQLModel, table=True):
    __tablename__ = "reservations"

    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="users.id", nullable=False)
    sala_id: int = Field(foreign_key="rooms.id", nullable=False)
    fecha: date = Field(nullable=False)
    hora_inicio: time = Field(nullable=False)
    hora_fin: time = Field(nullable=False)
    estado: str = Field(max_length=50, nullable=False)

    # Relaciones inversas
    usuario: Optional["User"] = Relationship(back_populates="reservations")
    sala: Optional["Room"] = Relationship(back_populates="reservations")