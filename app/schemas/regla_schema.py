from pydantic import BaseModel, condecimal


class ReglaOut(BaseModel):
    id: int
    monto_min: condecimal(max_digits=10, decimal_places=2)
    monto_max: condecimal(max_digits=10, decimal_places=2) | None
    porcentaje: condecimal(max_digits=5, decimal_places=2)

    class Config:
        orm_mode = True

class ReglaCreate(BaseModel):
    monto_min: condecimal(max_digits=10, decimal_places=2)
    monto_max: condecimal(max_digits=10, decimal_places=2) | None = None
    porcentaje: condecimal(max_digits=5, decimal_places=2)
