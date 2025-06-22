from decimal import Decimal
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.regla_model import Regla
from app.schemas.regla_schema import ReglaCreate


# ────────────────────────────────
# Leer la regla que aplica al total
# ────────────────────────────────
def get_por_total(session: Session, total: Decimal) -> Regla | None:
    """Devuelve la regla cuya franja cubre el total; None si no existe."""
    stmt = (
        select(Regla)
        .where(
            Regla.monto_min <= total,
            (Regla.monto_max == None) | (total <= Regla.monto_max)  # noqa: E711
        )
        .limit(1)
    )
    return session.scalars(stmt).first()


# ────────────────────────────────
# Crear una nueva regla de comisión
# ────────────────────────────────
def crear(session: Session, data: ReglaCreate) -> Regla:
    """Inserta una regla y la devuelve con su ID."""
    regla = Regla(**data.model_dump())  # model_dump() = dict() en Pydantic v2
    session.add(regla)
    session.commit()
    session.refresh(regla)
    return regla
