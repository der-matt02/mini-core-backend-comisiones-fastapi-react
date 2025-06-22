from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Crear el motor de conexión
engine = create_engine(settings.sqlalchemy_database_url, pool_pre_ping=True)

# Crear sesión para queries
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base para modelos ORM
Base = declarative_base()

def get_db():
    """Genera una sesión de BD y la cierra al finalizar la request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()