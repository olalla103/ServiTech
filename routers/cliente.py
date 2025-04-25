from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from models.cliente import Cliente
from schemas.usuario import UsuarioCreate  # Puedes crear un ClienteCreate si prefieres
from schemas.tecnico import TecnicoOut  # Reutiliza o crea ClienteOut
from typing import List

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TecnicoOut)
def crear_cliente(data: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_cliente = Cliente(**data.dict())
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente


@router.get("/", response_model=List[TecnicoOut])  # O ClienteOut si lo tienes separado
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()


@router.get("/{id}", response_model=TecnicoOut)  # O ClienteOut si tienes uno
def obtener_cliente(id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter_by(id=id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente
