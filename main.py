from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# main.py

from fastapi import FastAPI
from routers import tecnicos

app = FastAPI()

app.include_router(tecnicos.router)
