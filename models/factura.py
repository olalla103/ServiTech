# models/factura.py

# TODO: Ver factura específica
#       Listar facturas de un usuario autenticado
#       Añadir extras (trayectos,productos)
#       Generar factura de una reparación

from sqlalchemy import Column, String, DateTime, Float, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from db.db import Base
from datetime import datetime

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
    id_incidencia = Column(String(100), nullable=False)  # o Integer si es clave foránea
    id_tecnico = Column(String(100), nullable=False)
    id_cliente = Column(String(100), nullable=False)
    fecha_emision = Column(DateTime, default=datetime.utcnow)
    cantidad_adicional = Column(Float, default=0.0)
    cantidad_total = Column(Float, default=0.0)

    # Relación con productos (muchos a muchos)
    productos = relationship("Producto", secondary=factura_producto, back_populates="facturas")
