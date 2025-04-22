from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mariadb+pymysql://root:Nomevale4@localhost:3306/servitech"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# Manejador de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para los modelos
Base = declarative_base()
