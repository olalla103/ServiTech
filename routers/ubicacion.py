from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from models.ubicacion import Ubicacion
from models.incidencia import Incidencia
from schemas.ubicacion import UbicacionCreate, UbicacionOut

router = APIRouter(
    prefix="/ubicaciones",
    tags=["Ubicaciones"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UbicacionOut)
def registrar_ubicacion(data: UbicacionCreate, db: Session = Depends(get_db)):
    # Verificar que la incidencia existe
    incidencia = db.query(Incidencia).filter_by(id=data.incidencia_id).first()
    if not incidencia:
        raise HTTPException(status_code=404, detail="Incidencia no encontrada")

    # Verificar que no haya ya una ubicación asociada
    if incidencia.ubicacion:
        raise HTTPException(status_code=400, detail="Ya existe una ubicación para esta incidencia")

    # Confirmar automáticamente según lo que llega
    nueva_ubicacion = Ubicacion(
        incidencia_id=data.incidencia_id,
        latitud=data.latitud,
        longitud=data.longitud,
        direccion=data.direccion,
        confirmada=True,
        confirmada_por="sistema" if data.latitud and data.longitud else "cliente"
    )

    db.add(nueva_ubicacion)
    db.commit()
    db.refresh(nueva_ubicacion)
    return nueva_ubicacion

@router.get("/{incidencia_id}", response_model=UbicacionOut)
def obtener_ubicacion(incidencia_id: int, db: Session = Depends(get_db)):
    ubicacion = db.query(Ubicacion).filter_by(incidencia_id=incidencia_id).first()
    if not ubicacion:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    return ubicacion
