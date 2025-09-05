from sqlmodel import SQLModel, create_engine, Session

# Configuración de conexión (ajusta usuario/contraseña según XAMPP/phpMyAdmin)
DATABASE_URL = "mysql+pymysql://root:@localhost:3307/campusdev"

engine = create_engine(DATABASE_URL, echo=True)

# Dependencia para obtener sesión en FastAPI
def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
