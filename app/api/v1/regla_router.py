from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.regla_schema import ReglaCreate
from app.repositories.regla_repo import crear

router = APIRouter()


@router.post("/reglas")
def crear_regla(data: ReglaCreate, db: Session = Depends(get_db)):
    return crear(db, data)
