from datetime import datetime
from typing import Optional
from db.db import Base

from pydantic import Field


class Incidencia(Base):
    id_incidencia: str
    descripcion: Optional[str]
    estado: Optional[str] = "pendiente"
    fecha_reporte: Optional[datetime] = Field(default_factory=datetime.now)
