from pydantic import BaseModel
from datetime import date, time

class UserRead(BaseModel):
    id: int
    nombre: str
    email: str
    rol: str

    class Config:
        orm_mode = True

class RoomCreate(BaseModel):
    nombre: str
    sede: str
    capacidad: int
    recursos: str

class RoomRead(RoomCreate):
    id: int

    class Config:
        orm_mode = True

class ReservationCreate(BaseModel):
    sala_id: int
    fecha: date
    hora_inicio: time
    hora_fin: time

class ReservationRead(BaseModel):
    id: int
    usuario_id: int
    sala_id: int
    fecha: date
    hora_inicio: time
    hora_fin: time
    estado: str

    class Config:
        orm_mode = True
