from pydantic import BaseModel, condecimal


class ComisionOut(BaseModel):
    vendedor_id: int
    total_ventas: condecimal(max_digits=12, decimal_places=2)
    porcentaje_aplicado: condecimal(max_digits=5, decimal_places=2)
    comision: condecimal(max_digits=12, decimal_places=2)
