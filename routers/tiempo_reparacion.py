from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db import SessionLocal
from models.tiempo_reparacion import TiempoReparacion
from schemas.tiempo_reparacion import TiempoReparacionCreate, TiempoReparacionUpdate, TiempoReparacionOut

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
