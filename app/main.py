# el archivo main.py es el punto de entrada de la aplicación
from fastapi import FastAPI
from app.database.connection import Base, engine
from app.routes import auth, users, rooms, reservations

# Crear tablas en caso de que no existan
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Coworking Reservations API")

# Incluir routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(rooms.router)
app.include_router(reservations.router)
