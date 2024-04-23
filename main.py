from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

restaurantes = [
    {"nome": "Restaurante da tia Teteia", "status": "ativo"},
    {"nome": "Cantinho do Sabor", "status": "ativo"},
    {"nome": "Sabor Familiar", "status": "ativo"},
    {"nome": "Rancho da Vovó", "status": "ativo"},
    {"nome": "Sabor Caseiro", "status": "ativo"},
]


@app.get("/restaurantes/")
async def listar_restaurantes():
    return restaurantes


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
