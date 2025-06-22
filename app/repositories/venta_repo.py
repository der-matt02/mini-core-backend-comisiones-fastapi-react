from sqlalchemy.orm import Session
from app.models.venta_model import Venta  # ajusta el nombre si tu archivo es venta.py
from app.schemas.venta_schema import VentaCreate


def crear(session: Session, data: VentaCreate) -> Venta:
    """Inserta una venta y la devuelve con su ID."""
    venta = Venta(**data.model_dump())
    session.add(venta)
    session.commit()
    session.refresh(venta)
    return venta


def get_by_rango(session: Session, vendedor_id: int, start, end):
    return (
        session.query(Venta)
        .filter(
            Venta.vendedor_id == vendedor_id,
            Venta.fecha.between(start, end)
        )
        .all()
    )
