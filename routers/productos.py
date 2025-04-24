from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from models.producto import Producto
from schemas.producto import ProductoCreate, ProductoOut
from typing import List

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ProductoOut)
def crear_producto(data: ProductoCreate, db: Session = Depends(get_db)):
    producto = Producto(**data.dict())
    db.add(producto)
    db.commit()
    db.refresh(producto)
    return producto


@router.get("/", response_model=List[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()

@router.get("/{id}", response_model=ProductoOut)
def obtener_producto(id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter_by(id=id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

