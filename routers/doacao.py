# routers/doacao.py
from fastapi import APIRouter, HTTPException
from models.doacao import Doacao
from schemas.doacao import DoacaoCreate, DoacaoRead, DoacaoUpdate

router = APIRouter(prefix='/doacoes', tags=['Doações'])

@router.post('/', response_model=DoacaoRead)
def create_doacao(doacao: DoacaoCreate):
    new_doacao = Doacao.create(
        nome_animal=doacao.nome_animal,
        idade=doacao.idade,
        porte=doacao.porte,
        sexo=doacao.sexo,
        descricao=doacao.descricao,
        castrado=doacao.castrado,
        motivo_doacao=doacao.motivo_doacao,
        imagem=doacao.imagem
    )
    return new_doacao

@router.put('/{doacao_id}', response_model=DoacaoRead)
def update_doacao(doacao_id: int, doacao_data: DoacaoUpdate):
    doacao = Doacao.get_or_none(Doacao.id == doacao_id)

    if not doacao:
        raise HTTPException(status_code=404, detail="Doação não encontrada")

    doacao.nome_animal = doacao_data.nome_animal or doacao.nome_animal
    doacao.idade = doacao_data.idade or doacao.idade
    doacao.porte = doacao_data.porte or doacao.porte
    doacao.sexo = doacao_data.sexo or doacao.sexo
    doacao.descricao = doacao_data.descricao or doacao.descricao
    doacao.castrado = doacao_data.castrado if doacao_data.castrado is not None else doacao.castrado
    doacao.motivo_doacao = doacao_data.motivo_doacao or doacao.motivo_doacao
    doacao.imagem = doacao_data.imagem or doacao.imagem
    doacao.save()

    return doacao

@router.delete('/{doacao_id}', response_model=dict)
def delete_doacao(doacao_id: int):
    doacao = Doacao.get_or_none(Doacao.id == doacao_id)

    if not doacao:
        raise HTTPException(status_code=404, detail="Doação não encontrada")

    doacao.delete_instance()
    return {"message": "Doação deletada com sucesso"}

@router.get('/', response_model=list[DoacaoRead])
def get_all_doacoes():
    doacoes = Doacao.select()
    return list(doacoes)

@router.get('/{doacao_id}', response_model=DoacaoRead)
def get_doacao_by_id(doacao_id: int):
    doacao = Doacao.get_or_none(Doacao.id == doacao_id)

    if not doacao:
        raise HTTPException(status_code=404, detail="Doação não encontrada")

    return doacao
