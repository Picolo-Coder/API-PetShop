from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

# Modelo para criação de usuários
class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    cpf: str
    senha: str
    tipo_usuario: str

# Modelo para leitura de usuários (retorno)
class UsuarioRead(BaseModel):
    id: int
    nome: str
    email: EmailStr
    telefone: Optional[str] = None
    cpf: str
    tipo_usuario: str
    data_criacao: datetime

    class Config:
        orm_mode = True

# Modelo para atualização de usuários
class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    senha: Optional[str] = None
    tipo_usuario: Optional[str] = None
    cpf: Optional[str] = Field(None, example="123.456.789-00")

# Modelo para os dados de login
class LoginData(BaseModel):
    email: EmailStr
    senha: str
