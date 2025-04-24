from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from models.factura import Factura
from models.incidencia import Incidencia
from models.producto import Producto
from models.tiempo_reparacion import TiempoReparacion
from schemas.factura import FacturaCreate, FacturaOut, FacturaConfirm
from typing import List

router = APIRouter(
    prefix="/facturas",
    tags=["Facturas"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=FacturaOut)
def crear_factura(data: FacturaCreate, db: Session = Depends(get_db)):
    # Verificar que la incidencia existe
    incidencia = db.query(Incidencia).filter_by(id=data.id_incidencia).first()
    if not incidencia:
        raise HTTPException(status_code=404, detail="Incidencia no encontrada")

    # Verificar que no tenga factura previa
    if incidencia.factura:
        raise HTTPException(status_code=400, detail="Ya existe una factura para esta incidencia")

    # Calcular tiempo total desde los tiempos registrados
    tiempos = db.query(TiempoReparacion).filter_by(incidencia_id=incidencia.id).all()
    tiempo_total = 0
    for t in tiempos:
        if t.inicio and t.fin:
            tiempo_total += (t.fin - t.inicio).total_seconds() / 60

    # Crear factura
    factura = Factura(
        incidencia_id=incidencia.id,
        id_tecnico=data.id_tecnico,
        id_cliente=data.id_cliente,
        tiempo_total=int(tiempo_total),
        cantidad_adicional=data.cantidad_adicional,
        cantidad_total=data.cantidad_total
    )

    # Agregar productos
    productos = db.query(Producto).filter(Producto.id.in_(data.productos)).all()
    factura.productos = productos

    db.add(factura)
    db.commit()
    db.refresh(factura)
    return factura


@router.get("/", response_model=List[FacturaOut])
def listar_facturas(db: Session = Depends(get_db)):
    return db.query(Factura).all()


@router.get("/{id}", response_model=FacturaOut)
def obtener_factura(id: int, db: Session = Depends(get_db)):
    factura = db.query(Factura).filter_by(id=id).first()
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return factura


@router.put("/confirmar/{id}", response_model=FacturaOut)
def confirmar_factura(id: int, data: FacturaConfirm, db: Session = Depends(get_db)):
    factura = db.query(Factura).filter_by(id=id).first()
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

    factura.confirmada = data.confirmada
    db.commit()
    db.refresh(factura)
    return factura
