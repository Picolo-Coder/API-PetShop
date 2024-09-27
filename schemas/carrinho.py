from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class CarrinhoCreate(BaseModel):
    usuario_id: int
    produto_id: int
    tipo_produto: Literal['Camas', 'Casinhas', 'Brinquedos', 'Farmacia', 'Higiene', 'Alimentacao']
    quantidade: int = 1

class CarrinhoUpdate(BaseModel):
    usuario_id: int
    produto_id: int
    tipo_produto: Literal['Camas', 'Casinhas', 'Brinquedos', 'Farmacia', 'Higiene', 'Alimentacao']
    quantidade: int

class CarrinhoRead(BaseModel):
    id: int
    usuario_id: int
    produto_id: int
    tipo_produto: Literal['Camas', 'Casinhas', 'Brinquedos', 'Farmacia', 'Higiene', 'Alimentacao']
    quantidade: int

    class Config:
        orm_mode = True
