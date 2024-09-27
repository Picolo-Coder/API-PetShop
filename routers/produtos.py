from fastapi import APIRouter, HTTPException
from models.produtos import Produto
from schemas.produtos import ProdutoCreate, ProdutoRead, ProdutoUpdate

router = APIRouter(prefix='/produtos', tags=['Produtos'])


@router.post('/', response_model=ProdutoRead)
def create_produto(produto: ProdutoCreate):
    new_produto = Produto.create(
        nome=produto.nome,
        preco=produto.preco,
        descricao=produto.descricao,
        volume=produto.volume,
        imagem=produto.imagem,
        tipo=produto.tipo_id
    )
    return new_produto


@router.put('/{produto_id}', response_model=ProdutoRead)
def update_produto(produto_id: int, produto_data: ProdutoUpdate):
    produto = Produto.get_or_none(Produto.id == produto_id)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    produto.nome = produto_data.nome or produto.nome
    produto.preco = produto_data.preco or produto.preco
    produto.descricao = produto_data.descricao or produto.descricao
    produto.volume = produto_data.volume or produto.volume
    produto.imagem = produto_data.imagem or produto.imagem
    produto.tipo = produto_data.tipo_id or produto.tipo
    produto.save()

    return produto


@router.delete('/{produto_id}', response_model=dict)
def delete_produto(produto_id: int):
    produto = Produto.get_or_none(Produto.id == produto_id)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    produto.delete_instance()
    return {"message": "Produto deletado com sucesso"}


@router.get('/', response_model=list[ProdutoRead])
def get_produtos():
    produtos = Produto.select()
    return list(produtos)


@router.get('/{produto_id}', response_model=ProdutoRead)
def get_produto_by_id(produto_id: int):
    produto = Produto.get_or_none(Produto.id == produto_id)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto
