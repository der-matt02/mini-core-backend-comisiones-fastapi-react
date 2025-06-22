from sqlalchemy import Column, Integer, Date, ForeignKey, DECIMAL
from app.core.database import Base


class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    vendedor_id = Column(Integer, ForeignKey("vendedores.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    monto = Column(DECIMAL(10, 2), nullable=False)
