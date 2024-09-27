# schemas/doacao.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DoacaoBase(BaseModel):
    nome_animal: str
    idade: int
    porte: str   # 'pequeno', 'medio', 'grande'
    sexo: str    # 'macho', 'femea'
    descricao: Optional[str] = None
    castrado: bool = False
    motivo_doacao: Optional[str] = None
    imagem: str

class DoacaoCreate(DoacaoBase):
    pass

class DoacaoUpdate(BaseModel):
    nome_animal: Optional[str] = None
    idade: Optional[int] = None
    porte: Optional[str] = None
    sexo: Optional[str] = None
    descricao: Optional[str] = None
    castrado: Optional[bool] = None
    motivo_doacao: Optional[str] = None
    imagem: Optional[str] = None

class DoacaoRead(DoacaoBase):
    id: int

    class Config:
        orm_mode = True
