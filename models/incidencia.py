from sqlalchemy import Column, Enum, Integer, Text, DateTime, String

from datetime import datetime
from typing import Optional

from sqlalchemy.orm import relationship

from db.db import Base

from pydantic import Field

from models.enums import EstadoIncidencia


class Incidencia(Base):
    __tablename__ = "incidencias"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(Text, nullable=False)
    fecha_reporte = Column(DateTime, default=datetime.utcnow)
    estado = Column(Enum(EstadoIncidencia), default=EstadoIncidencia.pendiente, nullable=False)

    cliente_uid = Column(String(128), nullable=False)
    tecnico_uid = Column(String(128), nullable=True)

    # Relación con tiempos y factura
    factura = relationship("Factura", back_populates="incidencia", uselist=False)
    tiempos = relationship("TiempoReparacion", back_populates="incidencia")

