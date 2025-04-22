# File: models/producto.py

# TODO: Obtener listado de productos
#     Registrar nuevo producto (si no existe)
#     Solicitar producto no disponible

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from db.db import Base


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)

    # Relación con facturas
    facturas = relationship("Factura", secondary="factura_producto", back_populates="productos")
