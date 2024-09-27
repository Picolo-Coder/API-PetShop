from fastapi import APIRouter, HTTPException
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate, UsuarioRead, UsuarioUpdate
from peewee import IntegrityError
from datetime import datetime

router = APIRouter(prefix='/usuarios', tags=['Usuários'])


@router.post('/', response_model=UsuarioRead)
def create_usuario(usuario: UsuarioCreate):
    try:
        new_usuario = Usuario.create(
            nome=usuario.nome,
            email=usuario.email,
            telefone=usuario.telefone,
            senha=usuario.senha,
            cpf=usuario.cpf,
            tipo_usuario=usuario.tipo_usuario,
            data_criacao = datetime.now()
        )
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Usuário com e-mail ou CPF já existe")

    return new_usuario


@router.put('/{usuario_id}', response_model=UsuarioRead)
def update_usuario(usuario_id: int, usuario_data: UsuarioUpdate):
    usuario = Usuario.get_or_none(Usuario.id == usuario_id)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Atualiza os campos, incluindo o CPF
    usuario.nome = usuario_data.nome or usuario.nome
    usuario.email = usuario_data.email or usuario.email
    usuario.telefone = usuario_data.telefone or usuario.telefone
    usuario.senha = usuario_data.senha or usuario.senha
    usuario.tipo_usuario = usuario_data.tipo_usuario or usuario.tipo_usuario
    usuario.cpf = usuario_data.cpf or usuario.cpf  # Adicione esta linha para atualizar o CPF

    usuario.save()

    return usuario



@router.delete('/{usuario_id}', response_model=dict)
def delete_usuario(usuario_id: int):
    usuario = Usuario.get_or_none(Usuario.id == usuario_id)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario.delete_instance()
    return {"message": "Usuário deletado com sucesso"}


@router.get('/', response_model=list[UsuarioRead])
def get_usuarios():
    usuarios = Usuario.select()
    return list(usuarios)


@router.get('/{usuario_id}', response_model=UsuarioRead)
def get_usuario_by_id(usuario_id: int):
    usuario = Usuario.get_or_none(Usuario.id == usuario_id)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return usuario