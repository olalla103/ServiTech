# File: models/tecnico.py

# TODO: iniciar reparación con validación de ubicación
#       iniciar reparación sin validación de ubicación
#       Pausar reparación (causa justificada)
#       Reanudar reparación
#       Finalizar reparación
#       Cancelar reparación
#       Historial reparaciones del técnico

from sqlalchemy import Column, Integer, String
from db.db import Base
from models.usuario import Usuario


class Tecnico(Base, Usuario):
    __tablename__ = "tecnicos"

    id = Column(Integer, primary_key=True, index=True)
    especialidad = Column(String(100))
    empresa = Column(String(100))
