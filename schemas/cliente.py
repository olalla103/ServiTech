from pydantic import BaseModel, validator


class Cliente(BaseModel):
    telefono: str

    @validator("telefono")
    def validar_telefono(cls, v):
        import re
        if not re.fullmatch(r'\+?\d{9,15}', v):
            raise ValueError("Número de teléfono inválido")
        return v
