from datetime import date
from decimal import Decimal
from sqlalchemy.orm import Session
from app.repositories import venta_repo, regla_repo


def calcular_comision(
        db: Session, vendedor_id: int, start: date, end: date
) -> dict:
    ventas = venta_repo.get_by_rango(db, vendedor_id, start, end)
    total = sum(v.monto for v in ventas) if ventas else Decimal(0)

    regla = regla_repo.get_por_total(db, total)
    porcentaje = regla.porcentaje if regla else Decimal(0)

    comision = total * (porcentaje / Decimal(100))

    return {
        "vendedor_id": vendedor_id,
        "total_ventas": total,
        "porcentaje_aplicado": porcentaje,
        "comision": comision,
    }
