from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.room.RoomModel import Room
from app.models.schemas import RoomCreate, RoomRead
from app.auth.auth import get_current_user, verify_admin

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.get("/", response_model=list[RoomRead])
def list_rooms(session: Session = Depends(get_session)):
    rooms = session.exec(select(Room)).all()
    return rooms

@router.post("/", response_model=RoomRead, status_code=status.HTTP_201_CREATED, dependencies=[Depends(verify_admin)])
def create_room(room: RoomCreate, session: Session = Depends(get_session)):
    db_room = Room.from_orm(room)
    session.add(db_room)
    session.commit()
    session.refresh(db_room)
    return db_room


@router.put("/{room_id}", response_model=RoomRead, dependencies=[Depends(verify_admin)])
def update_room(room_id: int, room: RoomCreate, session: Session = Depends(get_session)):
    db_room = session.get(Room, room_id)
    if not db_room:
        raise HTTPException(status_code=404, detail="Room not found")
    for key, value in room.dict().items():
        setattr(db_room, key, value)
    session.add(db_room)
    session.commit()
    session.refresh(db_room)
    return db_room


@router.delete("/{room_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(verify_admin)])
def delete_room(room_id: int, session: Session = Depends(get_session)):
    db_room = session.get(Room, room_id)
    if not db_room:
        raise HTTPException(status_code=404, detail="Room not found")
    session.delete(db_room)
    session.commit()

