# schemas / incidencia.py

from pydantic import BaseModel, field_validator
from typing import Optional

from datetime import datetime
from models.enums import EstadoIncidencia


class IncidenciaCreate(BaseModel):
    id_cliente: str
    id_tecnico: str
    descripcion: str
    fecha_inicio: datetime
    fecha_fin: Optional[datetime] = None
    estado: Optional[EstadoIncidencia] = EstadoIncidencia.pendiente
    direccion: str


class IncidenciaUpdate(BaseModel):
    estado: Optional[EstadoIncidencia] = None
    fecha_fin: Optional[str] = None  # o datetime si lo manejas así


class IncidenciaOut(BaseModel):
    id: int
    uid_cliente: str
    uid_tecnico: str
    descripcion: str
    fecha_inicio: datetime
    fecha_fin: Optional[datetime] = None
    estado: Optional[EstadoIncidencia] = EstadoIncidencia.pendiente  # Por defecto, la incidencia se encuentra pendiente
    direccion: str

    class Config:
        orm_mode = True
