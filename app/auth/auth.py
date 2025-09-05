from datetime import timedelta, datetime
from typing import Annotated, Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select
from starlette import status
from app.core.database import get_session
from app.models.user.UserModel import User
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

SECRET_KEY = "09d25e094faa6ca2556c8c65d2f632e24f92cacdc8d098f25b7379c7"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

class CreateUserRequest(BaseModel):
    nombre: str
    email: str
    password: str
    rol: str = "user"

class Token(BaseModel):
    access_token: str
    token_type: str

db_dependency = Annotated[Session, Depends(get_session)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    db: db_dependency,
    create_user_request: CreateUserRequest
):
    user = User(
        nombre=create_user_request.nombre,
        email=create_user_request.email,
        contraseña_hash=bcrypt_context.hash(create_user_request.password),
        rol=create_user_request.rol
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(user.email, user.id, user.rol, timedelta(minutes=20))
    return {"access_token": token, "token_type": "bearer"}

def authenticate_user(username: str, password: str, db: Session) -> Optional[User]:
    statement = select(User).where(User.email == username)
    user = db.exec(statement).first()
    if not user:
        return None
    if not bcrypt_context.verify(password, user.contraseña_hash):
        return None
    return user

def create_access_token(username: str, user_id: int, rol: str, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id, "rol": rol}
    expires = datetime.utcnow() + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        email = payload.get("email")
        rol = payload.get("rol")
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials")
        return {"email": email, "rol": rol}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials")

def verify_admin(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        rol = payload.get("rol")
        if rol != "admin":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins can access this resource")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials")    

auth = router