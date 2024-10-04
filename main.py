from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import (
    banhotosa,
    carrinho,
    doacao,
    produtos,
    tipos,
    usuario,
)
from config.database import startup_db, shutdown_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler('startup', startup_db)
app.add_event_handler('shutdown', shutdown_db)

# Incluindo os routers
app.include_router(banhotosa.router)
app.include_router(carrinho.router)
app.include_router(doacao.router)
app.include_router(produtos.router)
app.include_router(tipos.router)
app.include_router(usuario.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Petshop"}

# Ouvindo as conexões no localhost:8000 por padrão
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
