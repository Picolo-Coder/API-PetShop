from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile
from datetime import datetime

class DoacaoBase(BaseModel):
    nome_animal: str
    idade: int
    porte: str  # 'pequeno', 'medio', 'grande'
    sexo: str   # 'macho', 'femea'
    descricao: Optional[str] = None
    castrado: bool = False
    motivo_doacao: Optional[str] = None
    data_criacao: datetime = datetime.now()  # Campo para registrar a data de criação

class DoacaoCreate(DoacaoBase):
    imagem: UploadFile  # O campo imagem será tratado como um arquivo

class DoacaoUpdate(BaseModel):
    nome_animal: Optional[str] = None
    idade: Optional[int] = None
    porte: Optional[str] = None
    sexo: Optional[str] = None
    descricao: Optional[str] = None
    castrado: Optional[bool] = None
    motivo_doacao: Optional[str] = None
    imagem: Optional[UploadFile] = None  # Agora, a imagem é opcional no update

class DoacaoRead(DoacaoBase):
    id: int
    imagem: str  # No DoacaoRead, armazenamos o caminho da imagem como string para retornar a URL.

    class Config:
        orm_mode = True
