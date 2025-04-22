# File: schemas/usuario.py

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UsuarioCreate(BaseModel):
    nombre: str
    apellido1: str
    apellido2: Optional[str]
    telefono: str
    email: EmailStr
    nombreUsuario: str
    contrasenia: str
    fecha_nacimiento: datetime
    DNI: str
    tecnico: Optional[bool] = False
