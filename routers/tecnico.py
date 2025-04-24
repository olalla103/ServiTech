from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from models.tecnico import Tecnico
from schemas.tecnico import TecnicoCreate, TecnicoOut
from typing import List

router = APIRouter(
    prefix="/tecnicos",
    tags=["Técnicos"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TecnicoOut)
def crear_tecnico(data: TecnicoCreate, db: Session = Depends(get_db)):
    nuevo_tecnico = Tecnico(**data.dict())
    db.add(nuevo_tecnico)
    db.commit()
    db.refresh(nuevo_tecnico)
    return nuevo_tecnico


@router.get("/", response_model=List[TecnicoOut])
def listar_tecnicos(db: Session = Depends(get_db)):
    return db.query(Tecnico).all()


@router.get("/{id}", response_model=TecnicoOut)
def obtener_tecnico(id: int, db: Session = Depends(get_db)):
    tecnico = db.query(Tecnico).filter_by(id=id).first()
    if not tecnico:
        raise HTTPException(status_code=404, detail="Técnico no encontrado")
    return tecnico
