# File: models/usuario.py

# TODO registrar usuario
#         iniciar sesion
#         cerrar sesion
#         obtener datos usuario
#         modificar datos usuario
#         eliminar usuario
#         listar usuarios

from sqlalchemy import Column, String, DateTime


class Usuario:
    DNI = Column(String(10), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido1 = Column(String(100), nullable=False)
    apellido2 = Column(String(100))
    telefono = Column(String(20))
    email = Column(String(150), unique=True, nullable=False)
    nombreUsuario = Column(String(50), unique=True, nullable=False)
    contrasenia = Column(String(255), nullable=False)
    fecha_nacimiento = Column(DateTime)
