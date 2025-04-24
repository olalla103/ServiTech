# models/tiempo_reparacion.py

from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.db import Base


class TiempoReparacion(Base):
    __tablename__ = "tiempo_reparacion"

    id = Column(Integer, primary_key=True, index=True)
    incidencia_id = Column(Integer, ForeignKey("incidencias.id"), nullable=False)
    tecnico_uid = Column(String(128), nullable=False)  # Firebase UID
    inicio = Column(DateTime, default=datetime.utcnow, nullable=False)
    pausa = Column(DateTime, nullable=True)
    reanudacion = Column(DateTime, nullable=True)
    fin = Column(DateTime, nullable=True)
    motivo_pausa = Column(String(255), nullable=True)


    # Relación con la incidencia
    incidencia = relationship("Incidencia", back_populates="tiempos")
