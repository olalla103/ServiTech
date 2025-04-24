from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from models.incidencia import Incidencia
from schemas.incidencia import IncidenciaCreate, IncidenciaOut
from typing import List

router = APIRouter(
    prefix="/incidencias",
    tags=["Incidencias"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=IncidenciaOut)
def crear_incidencia(data: IncidenciaCreate, db: Session = Depends(get_db)):
    nueva = Incidencia(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@router.get("/", response_model=List[IncidenciaOut])
def listar_incidencias(db: Session = Depends(get_db)):
    return db.query(Incidencia).all()


@router.get("/{id}", response_model=IncidenciaOut)
def obtener_incidencia(id: int, db: Session = Depends(get_db)):
    incidencia = db.query(Incidencia).filter_by(id=id).first()
    if not incidencia:
        raise HTTPException(status_code=404, detail="Incidencia no encontrada")
    return incidencia


@router.get("/{id}", response_model=IncidenciaOut)
def obtener_incidencia(id: int, db: Session = Depends(get_db)):
    incidencia = db.query(Incidencia).filter_by(id=id).first()
    if not incidencia:
        raise HTTPException(status_code=404, detail="Incidencia no encontrada")
    return incidencia


from schemas.incidencia import IncidenciaUpdate


@router.put("/{id}", response_model=IncidenciaOut)
def actualizar_estado_incidencia(id: int, data: IncidenciaUpdate, db: Session = Depends(get_db)):
    incidencia = db.query(Incidencia).filter_by(id=id).first()
    if not incidencia:
        raise HTTPException(status_code=404, detail="Incidencia no encontrada")

    for clave, valor in data.model_dump(exclude_unset=True).items():
        setattr(incidencia, clave, valor)

    db.commit()
    db.refresh(incidencia)
    return incidencia
