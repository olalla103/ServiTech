from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TiempoReparacionCreate(BaseModel):
    incidencia_id: int
    tecnico_uid: str


class TiempoReparacionUpdate(BaseModel):
    pausa: Optional[datetime] = None
    reanudacion: Optional[datetime] = None
    fin: Optional[datetime] = None
    motivo_pausa: Optional[str] = None


class TiempoReparacionOut(BaseModel):
    id: int
    incidencia_id: int
    tecnico_uid: str
    inicio: datetime
    pausa: Optional[datetime]
    reanudacion: Optional[datetime]
    fin: Optional[datetime]
    motivo_pausa: Optional[str]

    class Config:
        orm_mode = True
