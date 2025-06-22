from datetime import date
from pydantic import BaseModel, condecimal


class VentaBase(BaseModel):
    vendedor_id: int
    fecha: date
    monto: condecimal(max_digits=10, decimal_places=2)


class VentaCreate(VentaBase):
    pass


class VentaOut(VentaBase):
    id: int

    class Config:
        orm_mode = True
