from sqlalchemy.orm import Session
from app.repositories import vendedor_repo
from app.schemas.vendedor_schema import VendedorCreate


def crear_vendedor(db: Session, data: VendedorCreate):
    return vendedor_repo.crear(db, data)


def listar_vendedores(db: Session):
    return vendedor_repo.get_all(db)
