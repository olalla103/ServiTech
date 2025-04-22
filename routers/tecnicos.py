# routers/tecnicos.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db import SessionLocal
from models.tecnico import Tecnico
from schemas.tecnico import TecnicoCreate, TecnicoOut

router = APIRouter(
    prefix="/tecnicos",
    tags=["Técnicos"]
)

# Obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear técnico
@router.post("/", response_model=TecnicoOut)
def crear_tecnico(data: TecnicoCreate, db: Session = Depends(get_db)):
    nuevo_tecnico = Tecnico(**data.dict())
    db.add(nuevo_tecnico)
    db.commit()
    db.refresh(nuevo_tecnico)
    return nuevo_tecnico

# Listar técnicos
@router.get("/", response_model=list[TecnicoOut])
def listar_tecnicos(db: Session = Depends(get_db)):
    return db.query(Tecnico).all()
