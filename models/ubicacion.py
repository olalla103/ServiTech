from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from fecha_utils import datetime
from db.db import Base

class Ubicacion(Base):
    __tablename__ = "ubicaciones"

    id = Column(Integer, primary_key=True, index=True)
    incidencia_id = Column(Integer, ForeignKey("incidencias.id"), unique=True, nullable=False)

    latitud = Column(String(50), nullable=True)
    longitud = Column(String(50), nullable=True)
    direccion = Column(String(255), nullable=True)

    confirmada = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)

    incidencia = relationship("Incidencia", back_populates="ubicacion")
