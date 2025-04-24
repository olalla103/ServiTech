from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from models.tiempo_reparacion import TiempoReparacion
from schemas.tiempo_reparacion import TiempoReparacionCreate, TiempoReparacionUpdate, TiempoReparacionOut
from typing import List

router = APIRouter(
    prefix="/tiempos",
    tags=["Tiempos de reparación"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TiempoReparacionOut)
def iniciar_tiempo(data: TiempoReparacionCreate, db: Session = Depends(get_db)):
    nuevo = TiempoReparacion(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.put("/{id}", response_model=TiempoReparacionOut)
def actualizar_tiempo(id: int, data: TiempoReparacionUpdate, db: Session = Depends(get_db)):
    tiempo = db.query(TiempoReparacion).filter_by(id=id).first()
    for key, value in data.dict(exclude_unset=True).items():
        setattr(tiempo, key, value)
    db.commit()
    db.refresh(tiempo)
    return tiempo


@router.get("/", response_model=List[TiempoReparacionOut])
def listar_tiempos(db: Session = Depends(get_db)):
    return db.query(TiempoReparacion).all()


@router.get("/{id}", response_model=TiempoReparacionOut)
def obtener_tiempo(id: int, db: Session = Depends(get_db)):
    tiempo = db.query(TiempoReparacion).filter_by(id=id).first()
    if not tiempo:
        raise HTTPException(status_code=404, detail="Registro de tiempo no encontrado")
    return tiempo


from schemas.tiempo_reparacion import TiempoReparacionUpdate


@router.put("/{id}", response_model=TiempoReparacionOut)
def actualizar_tiempo(id: int, data: TiempoReparacionUpdate, db: Session = Depends(get_db)):
    tiempo = db.query(TiempoReparacion).filter_by(id=id).first()
    if not tiempo:
        raise HTTPException(status_code=404, detail="Registro de tiempo no encontrado")

    # Solo actualiza los campos que llegan (gracias a exclude_unset=True)
    for clave, valor in data.model_dump(exclude_unset=True).items():
        setattr(tiempo, clave, valor)

    db.commit()
    db.refresh(tiempo)
    return tiempo
