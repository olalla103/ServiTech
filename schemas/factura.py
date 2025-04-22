# File: schemas/factura.py

from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from schemas.producto import ProductoOut  # Lo necesitas definido


class FacturaCreate(BaseModel):
    id_incidencia: str
    id_tecnico: str
    id_cliente: str
    cantidad_adicional: float
    cantidad_total: float
    productos: Optional[List[int]] = []  # IDs de productos


class FacturaOut(BaseModel):
    id: int
    id_incidencia: str
    id_tecnico: str
    id_cliente: str
    fecha_emision: datetime
    cantidad_adicional: float
    cantidad_total: float
    productos: List[ProductoOut] = []  # objetos completos de productos

    class Config:
        orm_mode = True
