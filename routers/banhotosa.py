from fastapi import APIRouter, HTTPException
from models.banhotosa import BanhoTosa
from models.usuario import Usuario
from schemas.banhotosa import BanhoTosaCreate, BanhoTosaRead, BanhoTosaUpdate

router = APIRouter(prefix='/banho-tosa', tags=['Banho e Tosa'])


@router.post('/', response_model=BanhoTosaRead)
def create_banho_tosa(banho_tosa: BanhoTosaCreate):
    usuario = Usuario.get_or_none(Usuario.id == banho_tosa.usuario_id)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    new_banho_tosa = BanhoTosa.create(
        usuario=usuario,
        tipo_servico=banho_tosa.tipo_servico,
        data_reserva=banho_tosa.data_reserva
    )
    return new_banho_tosa


@router.put('/{banho_tosa_id}', response_model=BanhoTosaRead)
def update_banho_tosa(banho_tosa_id: int, banho_tosa_data: BanhoTosaUpdate):
    banho_tosa = BanhoTosa.get_or_none(BanhoTosa.id == banho_tosa_id)

    if not banho_tosa:
        raise HTTPException(status_code=404, detail="Banho e Tosa não encontrado")

    banho_tosa.usuario = banho_tosa_data.usuario_id or banho_tosa.usuario
    banho_tosa.tipo_servico = banho_tosa_data.tipo_servico or banho_tosa.tipo_servico
    banho_tosa.data_reserva = banho_tosa_data.data_reserva or banho_tosa.data_reserva
    banho_tosa.save()

    return banho_tosa


@router.delete('/{banho_tosa_id}', response_model=dict)
def delete_banho_tosa(banho_tosa_id: int):
    banho_tosa = BanhoTosa.get_or_none(BanhoTosa.id == banho_tosa_id)

    if not banho_tosa:
        raise HTTPException(status_code=404, detail="Banho e Tosa não encontrado")

    banho_tosa.delete_instance()
    return {"message": "Banho e Tosa deletado com sucesso"}


@router.get('/', response_model=list[BanhoTosaRead])
def get_banho_tosas_by_usuario(usuario_id: int):
    usuario = Usuario.get_or_none(Usuario.id == usuario_id)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    banho_tosas = BanhoTosa.select().where(BanhoTosa.usuario == usuario)
    return list(banho_tosas)


@router.get('/{banho_tosa_id}', response_model=BanhoTosaRead)
def get_banho_tosa_by_id(banho_tosa_id: int):
    banho_tosa = BanhoTosa.get_or_none(BanhoTosa.id == banho_tosa_id)

    if not banho_tosa:
        raise HTTPException(status_code=404, detail="Banho e Tosa não encontrado")

    return banho_tosa
