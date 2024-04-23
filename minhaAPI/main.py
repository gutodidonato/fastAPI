from fastapi import FastAPI
import uvicorn

app = FastAPI()

restaurante = {
    1: {"nome": "Restaurante da tia Teteia", "status": "ativo"},
    2: {"nome": "Cantinho do Sabor", "status": "ativo"},
    3: {"nome": "Sabor Familiar", "status": "ativo"},
    4: {"nome": "Rancho da Vovó", "status": "ativo"},
    5: {"nome": "Sabor Caseiro", "status": "ativo"},
}


@app.get("/restaurante/{id_restaurante}")
def pegar_restaurante(id_restaurante: int):
    if id_restaurante in restaurante:
        return restaurante[id_restaurante]
    else:
        return {"erro": f"Não existe um Restaurante com o ID {id_restaurante}"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
