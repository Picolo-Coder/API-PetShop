from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from models.doacao import Doacao
from schemas.doacao import DoacaoCreate, DoacaoRead, DoacaoUpdate
import os
from uuid import uuid4
from fastapi.responses import FileResponse

router = APIRouter(prefix='/doacoes', tags=['Doações'])

# Diretório onde as imagens serão armazenadas
IMAGENS_DIR = "imagens_doacoes/"

# Função para salvar a imagem no servidor
def save_image(imagem: UploadFile) -> str:
    if not os.path.exists(IMAGENS_DIR):
        os.makedirs(IMAGENS_DIR)

    extension = imagem.filename.split('.')[-1]
    filename = f"{uuid4()}.{extension}"  # Gera um nome único
    image_path = os.path.join(IMAGENS_DIR, filename)

    with open(image_path, "wb") as buffer:
        buffer.write(imagem.file.read())

    return image_path

# Função para deletar a imagem do servidor
def delete_image(image_path: str):
    if image_path and os.path.exists(image_path):
        os.remove(image_path)

# POST - Criar uma nova doação (com imagem)
@router.post('/', response_model=DoacaoRead)
async def create_doacao(
    nome_animal: str = Form(...),
    idade: int = Form(...),
    porte: str = Form(...),
    sexo: str = Form(...),
    descricao: str = Form(...),
    castrado: bool = Form(...),
    motivo_doacao: str = Form(...),
    imagem: UploadFile = File(...)  # Adiciona o campo de upload de imagem
):
    # Salva a imagem e obtém o caminho
    imagem_path = save_image(imagem)

    new_doacao = Doacao.create(
        nome_animal=nome_animal,
        idade=idade,
        porte=porte,
        sexo=sexo,
        descricao=descricao,
        castrado=castrado,
        motivo_doacao=motivo_doacao,
        imagem=imagem_path  # Armazena o caminho da imagem
    )
    return new_doacao

# PUT - Atualizar doação (campos de formulário e imagem opcional)
@router.put('/{doacao_id}', response_model=DoacaoRead)
async def update_doacao(
    doacao_id: int,
    nome_animal: str = Form(None),
    idade: int = Form(None),
    porte: str = Form(None),
    sexo: str = Form(None),
    descricao: str = Form(None),
    castrado: bool = Form(None),
    motivo_doacao: str = Form(None),
    imagem: UploadFile = File(None)  # Campo de imagem opcional
):
    doacao = Doacao.get_or_none(Doacao.id == doacao_id)

    if not doacao:
        raise HTTPException(status_code=404, detail="Doação não encontrada")

    # Atualiza os campos da doação se valores forem fornecidos
    doacao.nome_animal = nome_animal or doacao.nome_animal
    doacao.idade = idade or doacao.idade
    doacao.porte = porte or doacao.porte
    doacao.sexo = sexo or doacao.sexo
    doacao.descricao = descricao or doacao.descricao
    doacao.castrado = castrado if castrado is not None else doacao.castrado
    doacao.motivo_doacao = motivo_doacao or doacao.motivo_doacao

    # Se uma nova imagem for fornecida, atualiza-a
    if imagem:
        if doacao.imagem:  # Deletar a imagem antiga se houver
            delete_image(doacao.imagem)
        # Salva a nova imagem e atualiza o caminho
        imagem_path = save_image(imagem)
        doacao.imagem = imagem_path

    doacao.save()

    return doacao

# DELETE - Deletar doação e imagem associada
@router.delete('/{doacao_id}', response_model=dict)
async def delete_doacao(doacao_id: int):
    doacao = Doacao.get_or_none(Doacao.id == doacao_id)

    if not doacao:
        raise HTTPException(status_code=404, detail="Doação não encontrada")

    if doacao.imagem:
        delete_image(doacao.imagem)  # Deletar a imagem associada

    doacao.delete_instance()
    return {"message": "Doação e imagem deletadas com sucesso"}

# GET - Listar todas as doações
@router.get('/', response_model=list[DoacaoRead])
async def get_all_doacoes():
    doacoes = Doacao.select()
    return list(doacoes)

# GET - Buscar doação por ID
@router.get('/{doacao_id}', response_model=DoacaoRead)
async def get_doacao_by_id(doacao_id: int):
    doacao = Doacao.get_or_none(Doacao.id == doacao_id)

    if not doacao:
        raise HTTPException(status_code=404, detail="Doação não encontrada")

    return doacao

# GET - Retornar imagem da doação
@router.get('/{doacao_id}/imagem', response_class=FileResponse)
async def get_doacao_imagem(doacao_id: int):
    doacao = Doacao.get_or_none(Doacao.id == doacao_id)

    if not doacao or not doacao.imagem:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")

    return FileResponse(doacao.imagem)
