from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    descricao: Optional[str] = None
    volume: Optional[str] = None
    tipo_id: int

class ProdutoCreate(ProdutoBase):
    pass  # Removido o campo imagem

class ProdutoRead(ProdutoBase):
    id: int
    imagem: Optional[str]  # Aqui será o caminho da imagem armazenada

    class Config:
        orm_mode = True

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    preco: Optional[float] = None
    descricao: Optional[str] = None
    volume: Optional[str] = None
    tipo_id: Optional[int] = None
    # Removido o campo imagem