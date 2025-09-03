from fastapi import FastAPI, status, Depends, HTTPException
import models.users.UsersModel as UsersModel
from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI()

UsersModel.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/users")
def read_users(db: Session = Depends(db_dependency)):
    return UsersModel.get_all(db)

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(db_dependency)):
    return UsersModel.get_by_id(db, user_id)

@app.post("/users")
def create_user(user: UsersModel.User, db: Session = Depends(db_dependency)):
    return UsersModel.create(db, user)

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UsersModel.User, db: Session = Depends(db_dependency)):
    return UsersModel.update(db, user_id, user)

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(db_dependency)):
    return UsersModel.delete(db, user_id)

@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    return {"message": exc.detail}, exc.status_code

@app.exception_handler(Exception)
def exception_handler(request, exc):
    return {"message": "Internal Server Error"}, status.HTTP_500_INTERNAL_SERVER_ERROR  