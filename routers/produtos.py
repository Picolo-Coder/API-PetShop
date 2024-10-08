from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from models.produtos import Produto
from schemas.produtos import ProdutoCreate, ProdutoRead, ProdutoUpdate
import os
from uuid import uuid4
from fastapi.responses import FileResponse

router = APIRouter(prefix='/produtos', tags=['Produtos'])

# Diretório onde as imagens serão armazenadas
IMAGENS_DIR = "imagens_produtos/"

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

# POST - Criar um novo produto (com imagem)
@router.post('/', response_model=ProdutoRead)
async def create_produto(
    nome: str = Form(...),
    preco: float = Form(...),
    descricao: str = Form(...),
    volume: str = Form(...),
    tipo_id: int = Form(...),
    imagem: UploadFile = File(...)  # Adiciona o campo imagem
):
    # Salva a imagem e obtém o caminho
    imagem_path = save_image(imagem)

    new_produto = Produto.create(
        nome=nome,
        preco=preco,
        descricao=descricao,
        volume=volume,
        imagem=imagem_path,  # Armazena o caminho da imagem
        tipo=tipo_id
    )
    return new_produto

# PUT - Atualizar produto (campos de formulário e imagem opcional)
@router.put('/{produto_id}', response_model=ProdutoRead)
async def update_produto(
    produto_id: int,
    nome: str = Form(None),
    preco: float = Form(None),
    descricao: str = Form(None),
    volume: str = Form(None),
    tipo_id: int = Form(None),
    imagem: UploadFile = File(None)  # Campo de imagem opcional
):
    produto = Produto.get_or_none(Produto.id == produto_id)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    # Atualiza os campos do produto se valores forem fornecidos
    produto.nome = nome or produto.nome
    produto.preco = preco or produto.preco
    produto.descricao = descricao or produto.descricao
    produto.volume = volume or produto.volume
    produto.tipo = tipo_id or produto.tipo

    # Se uma nova imagem for fornecida, atualiza-a
    if imagem:
        if produto.imagem:  # Deletar a imagem antiga se houver
            delete_image(produto.imagem)
        # Salva a nova imagem e atualiza o caminho
        imagem_path = save_image(imagem)
        produto.imagem = imagem_path

    produto.save()

    return produto

# DELETE - Deletar produto e imagem associada
@router.delete('/{produto_id}', response_model=dict)
async def delete_produto(produto_id: int):
    produto = Produto.get_or_none(Produto.id == produto_id)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    if produto.imagem:
        delete_image(produto.imagem)  # Deletar a imagem do produto

    produto.delete_instance()
    return {"message": "Produto e imagem deletados com sucesso"}

# GET - Listar todos os produtos
@router.get('/', response_model=list[ProdutoRead])
async def get_produtos():
    produtos = Produto.select()
    return list(produtos)

# GET - Buscar produto por ID
@router.get('/{produto_id}', response_model=ProdutoRead)
async def get_produto_by_id(produto_id: int):
    produto = Produto.get_or_none(Produto.id == produto_id)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto

# GET - Retornar imagem do produto
@router.get('/{produto_id}/imagem', response_class=FileResponse)
async def get_produto_imagem(produto_id: int):
    produto = Produto.get_or_none(Produto.id == produto_id)

    if not produto or not produto.imagem:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")

    return FileResponse(produto.imagem)
