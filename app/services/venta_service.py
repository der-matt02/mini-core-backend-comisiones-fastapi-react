from sqlalchemy.orm import Session
from app.repositories import venta_repo
from app.schemas.venta_schema import VentaCreate


def crear_venta(db: Session, data: VentaCreate):
    return venta_repo.crear(db, data)
