# File: schemas/producto.py

from pydantic import BaseModel


class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str


class ProductoOut(BaseModel):
    id: int
    nombre: str
    descripcion: str

    class Config:
        orm_mode = True
