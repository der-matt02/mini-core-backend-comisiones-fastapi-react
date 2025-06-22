from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.venta_schema import VentaCreate, VentaOut
from app.repositories import venta_repo

venta_router = APIRouter(prefix="/ventas", tags=["Ventas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@venta_router.post("/", response_model=VentaOut)
def crear_venta(data: VentaCreate, db: Session = Depends(get_db)):
    return venta_repo.crear(db, data)
