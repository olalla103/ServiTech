from sqlalchemy import Column, Integer, String

from db.db import Base
from models.usuario import Usuario


class Cliente(Base, Usuario):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    direccion = Column(String(150))
