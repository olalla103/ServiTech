# schemas/tecnico.py

from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime


class TecnicoCreate(BaseModel):
    nombre: str
    apellido1: str
    apellido2: Optional[str]
    telefono: str
    email: EmailStr
    nombreUsuario: str
    contrasenia: str
    fecha_nacimiento: datetime
    DNI: str
    especialidad: str
    empresa: Optional[str]
    numero_seguridad_social: str
    autonomo: bool

    # Validación del DNI, que éste sea real
    @field_validator("DNI")
    @classmethod
    def comprobar_dni_valido(cls, v: str) -> str:
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(v) != 9 or not v[:-1].isdigit() or not v[-1].isalpha():
            raise ValueError("Formato de DNI incorrecto")
        numero = int(v[:-1])
        letra_correcta = letras[numero % 23]
        if v[-1].upper() != letra_correcta:
            raise ValueError("Letra del DNI no válida")
        return v

    @field_validator("contrasenia")
    @classmethod
    def validar_longitud_contrasenia(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        return v


class TecnicoOut(TecnicoCreate):
    id: int

    class Config:
        orm_mode = True
