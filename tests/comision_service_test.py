from datetime import date
from decimal import Decimal
from app.services.comision_service import calcular_comision
from app.models.vendedor_model import Vendedor
from app.models.venta_model import Venta
from app.models.regla_model import Regla


def test_calcular_comision(db_session):
    # ─────────── Arrange ───────────
    vendedor = Vendedor(nombre="Mario", apellido="Gómez")
    db_session.add(vendedor)
    db_session.commit()

    ventas = [
        Venta(vendedor_id=vendedor.id, fecha=date(2024, 1, 10), monto=Decimal("400")),
        Venta(vendedor_id=vendedor.id, fecha=date(2024, 1, 15), monto=Decimal("200")),
    ]
    reglas = [
        Regla(monto_min=Decimal("0"), monto_max=Decimal("500"), porcentaje=Decimal("5")),
        Regla(monto_min=Decimal("501"), monto_max=None, porcentaje=Decimal("10")),
    ]
    db_session.add_all(ventas + reglas)
    db_session.commit()

    # ─────────── Act ───────────
    result = calcular_comision(
        db_session,
        vendedor.id,
        date(2024, 1, 1),
        date(2024, 1, 31)
    )

    # ─────────── Assert ─────────
    assert result["total_ventas"] == Decimal("600")
    assert result["porcentaje_aplicado"] == Decimal("10")
    assert result["comision"] == Decimal("60")
