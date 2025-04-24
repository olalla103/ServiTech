# schemas/ubicacion.py

from pydantic import BaseModel, model_validator
from typing import Optional
from datetime import datetime


class UbicacionCreate(BaseModel):
    incidencia_id: int
    latitud: Optional[str] = None
    longitud: Optional[str] = None
    direccion: Optional[str] = None

    @model_validator(mode="after")
    def al_menos_una_ubicacion(cls, model):
        if not (model.latitud and model.longitud) and not model.direccion:
            raise ValueError("Debes proporcionar latitud y longitud o una dirección.")
        return model


class UbicacionOut(UbicacionCreate):
    id: int
    confirmada: bool
    fecha_registro: datetime

    class Config:
        orm_mode = True
