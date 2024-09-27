from pydantic import BaseModel

class TipoBase(BaseModel):
    nome_tipo: str

class TipoCreate(TipoBase):
    pass

class TipoRead(TipoBase):
    id: int

    class Config:
        orm_mode = True

class TipoUpdate(BaseModel):
    nome_tipo: str
