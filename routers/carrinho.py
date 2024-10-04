from fastapi import APIRouter, HTTPException
from models.carrinho import Carrinho
from models.usuario import Usuario
from models.produtos import Produto
from schemas.carrinho import CarrinhoCreate, CarrinhoRead, CarrinhoUpdate

router = APIRouter(prefix='/carrinhos', tags=['Carrinhos'])


@router.post('/', response_model=CarrinhoRead)
def create_carrinho(carrinho: CarrinhoCreate):
    # Verifica se o usuário existe
    usuario = Usuario.get_or_none(Usuario.id == carrinho.usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Verifica se o produto existe
    produto = Produto.get_or_none(Produto.id == carrinho.produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    # Cria um novo carrinho
    new_carrinho = Carrinho.create(
        usuario=usuario,
        produto=produto,
        quantidade=carrinho.quantidade
    )
    return new_carrinho


@router.put('/{carrinho_id}', response_model=CarrinhoRead)
def update_carrinho(carrinho_id: int, carrinho_data: CarrinhoUpdate):
    # Verifica se o carrinho existe
    carrinho = Carrinho.get_or_none(Carrinho.id == carrinho_id)
    if not carrinho:
        raise HTTPException(status_code=404, detail="Carrinho não encontrado")

    # Verifica se o usuário existe
    usuario = Usuario.get_or_none(Usuario.id == carrinho_data.usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Verifica se o produto existe
    produto = Produto.get_or_none(Produto.id == carrinho_data.produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    # Atualiza os campos do carrinho
    carrinho.usuario = usuario
    carrinho.produto = produto
    carrinho.quantidade = carrinho_data.quantidade
    carrinho.save()

    return carrinho


@router.delete('/{carrinho_id}', response_model=dict)
def delete_carrinho(carrinho_id: int):
    # Verifica se o carrinho existe
    carrinho = Carrinho.get_or_none(Carrinho.id == carrinho_id)
    if not carrinho:
        raise HTTPException(status_code=404, detail="Carrinho não encontrado")

    carrinho.delete_instance()
    return {"message": "Carrinho deletado com sucesso"}


@router.get('/', response_model=list[CarrinhoRead])
def get_all_carrinhos():
    # Retorna todos os carrinhos
    carrinhos = Carrinho.select()
    return list(carrinhos)


@router.get('/{carrinho_id}', response_model=CarrinhoRead)
def get_carrinho_by_id(carrinho_id: int):
    # Verifica se o carrinho existe
    carrinho = Carrinho.get_or_none(Carrinho.id == carrinho_id)
    if not carrinho:
        raise HTTPException(status_code=404, detail="Carrinho não encontrado")

    return carrinho
