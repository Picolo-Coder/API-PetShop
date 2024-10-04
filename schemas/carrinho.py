from pydantic import BaseModel

class CarrinhoCreate(BaseModel):
    usuario_id: int
    produto_id: int
    quantidade: int = 1

class CarrinhoUpdate(BaseModel):
    usuario_id: int
    produto_id: int
    quantidade: int

class CarrinhoRead(BaseModel):
    id: int
    usuario_id: int
    produto_id: int
    quantidade: int

    class Config:
        orm_mode = True
