from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.vendedor_model import Vendedor
from app.schemas.vendedor_schema import VendedorCreate


def crear(session: Session, data: VendedorCreate) -> Vendedor:
    vendedor = Vendedor(**data.model_dump())
    session.add(vendedor)
    session.commit()
    session.refresh(vendedor)
    return vendedor


def get_all(session: Session) -> list[Vendedor]:
    """Devuelve todos los vendedores como instancias tipadas correctamente."""
    stmt = select(Vendedor)
    return list(session.scalars(stmt))


def get_by_id(session: Session, vendedor_id: int) -> Vendedor | None:
    """Devuelve un vendedor por ID, o None si no existe."""
    stmt = select(Vendedor).where(Vendedor.id == vendedor_id)
    return session.scalars(stmt).first()
