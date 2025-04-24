# models/factura.py

# TODO: Ver factura específica
#       Listar facturas de un usuario autenticado
#       Añadir extras (trayectos,productos)
#       Generar factura de una reparación

from sqlalchemy import Column, String, Float, ForeignKey, Integer, Table, DateTime, Boolean
from sqlalchemy.orm import relationship
from db.db import Base
from fecha_utils import datetime

# Si hay relación muchos a muchos entre facturas y productos:
factura_producto = Table(
    'factura_producto',
    Base.metadata,
    Column('factura_id', Integer, ForeignKey('facturas.id')),
    Column('producto_id', Integer, ForeignKey('productos.id'))
)


class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True, index=True)
    incidencia_id = Column(Integer, ForeignKey("incidencias.id"), nullable=False, unique=True)
    id_tecnico = Column(String(100), nullable=False)  # Firebase UID
    id_cliente = Column(String(100), nullable=False)  # Firebase UID
    fecha_emision = Column(DateTime, default=datetime.utcnow, nullable=False)
    tiempo_total = Column(Integer, nullable=True)  # Tiempo total en minutos
    cantidad_adicional = Column(Float, default=0.0)
    cantidad_total = Column(Float, default=0.0)
    confirmada = Column(Boolean, default=False)

    # Relación con productos (muchos a muchos) y
    productos = relationship("Producto", secondary=factura_producto, back_populates="facturas")
    # Relación con la incidencia (1:1)
    incidencia = relationship("Incidencia", back_populates="factura")
