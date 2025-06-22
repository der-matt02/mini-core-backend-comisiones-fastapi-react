from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.vendedor_schema import VendedorCreate, VendedorOut
from app.services import vendedor_service

vendedor_router = APIRouter(prefix="/vendedores", tags=["Vendedores"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@vendedor_router.post("/", response_model=VendedorOut)
def crear_vendedor(data: VendedorCreate, db: Session = Depends(get_db)):
    return vendedor_service.crear_vendedor(db, data)


@vendedor_router.get("/", response_model=list[VendedorOut])
def listar_vendedores(db: Session = Depends(get_db)):
    return vendedor_service.listar_vendedores(db)
