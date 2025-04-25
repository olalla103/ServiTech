# main.py

from fastapi import FastAPI
from routers import tecnico, cliente, productos, incidencias, tiempos, factura, ubicacion

app = FastAPI()

# Incluir todos los routers
app.include_router(tecnico.router)
app.include_router(cliente.router)
app.include_router(productos.router)
app.include_router(incidencias.router)
app.include_router(tiempos.router)
app.include_router(factura.router)
app.include_router(ubicacion.router)


# Ruta base para probar que todo arranca
@app.get("/")
def root():
    return {"message": "La API está perfecta"}
