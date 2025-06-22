from sqlalchemy import Column, Integer, DECIMAL
from app.core.database import Base


class Regla(Base):
    __tablename__ = "reglas"

    id = Column(Integer, primary_key=True, index=True)
    monto_min = Column(DECIMAL(10, 2), nullable=False)
    monto_max = Column(DECIMAL(10, 2), nullable=True)
    porcentaje = Column(DECIMAL(5, 2), nullable=False)
