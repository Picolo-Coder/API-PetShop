from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BanhoTosaCreate(BaseModel):
    usuario_id: int
    tipo_servico: str
    data_reserva: datetime

class BanhoTosaUpdate(BaseModel):
    usuario_id: Optional[int] = None
    tipo_servico: Optional[str] = None
    data_reserva: Optional[datetime] = None

class BanhoTosaRead(BaseModel):
    id: int
    usuario_id: int
    tipo_servico: str
    data_reserva: datetime

    class Config:
        orm_mode = True