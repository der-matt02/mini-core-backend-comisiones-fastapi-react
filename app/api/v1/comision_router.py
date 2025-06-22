from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from app.core.database import SessionLocal
from app.services.comision_service import calcular_comision
from app.schemas.comision_schema import ComisionOut

comision_router = APIRouter(prefix="/comisiones", tags=["Comisiones"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@comision_router.get("/", response_model=ComisionOut)
def obtener_comision(
        vendedor_id: int,
        start: date,
        end: date,
        db: Session = Depends(get_db),
):
    return calcular_comision(db, vendedor_id, start, end)
