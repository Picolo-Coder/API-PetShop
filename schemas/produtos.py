from pydantic import BaseModel
from typing import Optional

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    descricao: Optional[str] = None
    volume: Optional[str] = None
    imagem: str
    tipo_id: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoRead(ProdutoBase):
    id: int

    class Config:
        orm_mode = True

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    preco: Optional[float] = None
    descricao: Optional[str] = None
    volume: Optional[str] = None
    imagem: Optional[str] = None
    tipo_id: Optional[int] = None
