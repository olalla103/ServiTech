# routers/incidencias.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db import SessionLocal
from models.incidencia import Incidencia
from schemas.incidencia import IncidenciaCreate, IncidenciaOut

router = APIRouter(
    prefix="/incidencias",
    tags=["Incidencias"]
)

# Para obtener una sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear una incidencia
@router.post("/", response_model=IncidenciaOut)
def crear_incidencia(data: IncidenciaCreate, db: Session = Depends(get_db)):
    nueva = Incidencia(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

# Obtener todas las incidencias
@router.get("/", response_model=list[IncidenciaOut])
def listar_incidencias(db: Session = Depends(get_db)):
    return db.query(Incidencia).all()
