# schemas/tecnico.py

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UsuarioBase(BaseModel):
    nombre: str
    apellido1: str
    apellido2: Optional[str] = None
    telefono: str
    email: EmailStr
    nombreUsuario: str
    contrasenia: str
    fecha_nacimiento: datetime
    DNI: str


class TecnicoCreate(UsuarioBase):
    especialidad: str
    empresa: str


class TecnicoOut(UsuarioBase):
    id: int
    especialidad: str
    empresa: str

    class Config:
        orm_mode = True
