from fastapi import APIRouter, HTTPException
from models.tipos import Tipo
from schemas.tipos import TipoCreate, TipoRead, TipoUpdate

router = APIRouter(prefix='/tipos', tags=['Tipos'])


@router.post('/', response_model=TipoRead)
def create_tipo(tipo: TipoCreate):
    if Tipo.get_or_none(Tipo.nome_tipo == tipo.nome_tipo):
        raise HTTPException(status_code=400, detail="Tipo já existe")

    new_tipo = Tipo.create(nome_tipo=tipo.nome_tipo)
    return new_tipo


@router.patch('/{tipo_id}', response_model=TipoRead)  # Mudança de PUT para PATCH
def update_tipo(tipo_id: int, tipo_data: TipoUpdate):
    tipo = Tipo.get_or_none(Tipo.id == tipo_id)

    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo não encontrado")

    # Atualiza apenas os campos fornecidos no tipo_data
    tipo.nome_tipo = tipo_data.nome_tipo if tipo_data.nome_tipo is not None else tipo.nome_tipo
    tipo.save()

    return tipo


@router.delete('/{tipo_id}', response_model=dict)
def delete_tipo(tipo_id: int):
    tipo = Tipo.get_or_none(Tipo.id == tipo_id)

    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo não encontrado")

    tipo.delete_instance()
    return {"message": "Tipo deletado com sucesso"}


@router.get('/', response_model=list[TipoRead])
def get_tipos():
    tipos = Tipo.select()
    return list(tipos)


@router.get('/{tipo_id}', response_model=TipoRead)
def get_tipo_by_id(tipo_id: int):
    tipo = Tipo.get_or_none(Tipo.id == tipo_id)

    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo não encontrado")

    return tipo
