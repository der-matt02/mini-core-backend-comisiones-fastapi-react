from pydantic import BaseModel


class VendedorBase(BaseModel):
    nombre: str
    apellido: str


class VendedorCreate(VendedorBase):
    pass


class VendedorOut(VendedorBase):
    id: int

    class Config:
        orm_mode = True
