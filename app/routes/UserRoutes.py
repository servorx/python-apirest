from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from starlette import status
from app.core.database import get_session
from app.models.user.UserModel import User
from app.auth.auth import get_current_user, verify_admin, oauth2_scheme, SECRET_KEY, ALGORITHM
from jose import jwt, JWTError

# esto sirve para definir la ruta de la API
router = APIRouter(
    prefix="/users",
    tags=["users"],
)

db_dependency = Annotated[Session, Depends(get_session)]

# esto es el endpoint que se va a llamar
@router.get("/me")
async def get_me(
    db: db_dependency,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("id")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token")
        statement = select(User).where(User.id == user_id)
        user = db.exec(statement).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found")
        return {"id": user.id, "nombre": user.nombre, "email": user.email, "rol": user.rol}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials")

# obtener todos los usuarios (solo admin)
@router.get("/")
async def get_all_users(
    db: db_dependency,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    if payload.get("rol") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can access this resource"
        )

    users = db.exec(select(User)).all()
    return users

# eliminar usuario (solo admin)
@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_user(
    id: int,
    db: db_dependency,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    if payload.get("rol").lower() != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can delete users"
        )

    statement = select(User).where(User.id == id)
    user = db.exec(statement).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}
