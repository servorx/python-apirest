from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.room.RoomModel import Room
from app.models.reservation.ReservationModel import Reservation
from app.models.schemas import ReservationCreate, ReservationRead
from app.auth.auth import get_current_user
from datetime import date

router = APIRouter(prefix="/reservations", tags=["reservations"])


@router.post("/", response_model=ReservationRead, status_code=status.HTTP_201_CREATED)
def create_reservation(reservation: ReservationCreate,
                       session: Session = Depends(get_session),
                       user: dict = Depends(get_current_user)):
    db_room = session.get(Room, reservation.sala_id)
    if not db_room:
        raise HTTPException(status_code=404, detail="Room not found")

    db_reservation = Reservation(
        usuario_id=user["id"],
        sala_id=reservation.sala_id,
        fecha=reservation.fecha,
        hora_inicio=reservation.hora_inicio,
        hora_fin=reservation.hora_fin,
        estado="pendiente"
    )
    session.add(db_reservation)
    session.commit()
    session.refresh(db_reservation)
    return db_reservation


@router.get("/me", response_model=list[ReservationRead])
def my_reservations(session: Session = Depends(get_session),
                    user: dict = Depends(get_current_user)):
    reservations = session.exec(
        select(Reservation).where(Reservation.usuario_id == user["id"])
    ).all()
    return reservations


@router.get("/room/{room_id}", response_model=list[ReservationRead])
def reservations_by_room(room_id: int,
                         session: Session = Depends(get_session)):
    reservations = session.exec(
        select(Reservation).where(Reservation.sala_id == room_id)
    ).all()
    return reservations


@router.get("/date/{reservation_date}", response_model=list[ReservationRead])
def reservations_by_date(reservation_date: date,
                         session: Session = Depends(get_session)):
    reservations = session.exec(
        select(Reservation).where(Reservation.fecha == reservation_date)
    ).all()
    return reservations


@router.delete("/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_reservation(reservation_id: int,
                       session: Session = Depends(get_session),
                       user: dict = Depends(get_current_user)):
    db_reservation = session.get(Reservation, reservation_id)
    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    if db_reservation.usuario_id != user["id"] and user["rol"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to cancel this reservation")
    db_reservation.estado = "cancelada"
    session.add(db_reservation)
    session.commit()
