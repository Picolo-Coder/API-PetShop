# routers/carrinho.py
from fastapi import APIRouter, HTTPException
from models.carrinho import Carrinho
from models.usuario import Usuario
from schemas.carrinho import CarrinhoCreate, CarrinhoRead, CarrinhoUpdate

router = APIRouter(prefix='/carrinhos', tags=['Carrinhos'])

@router.post('/', response_model=CarrinhoRead)
def create_carrinho(carrinho: CarrinhoCreate):
    usuario = Usuario.get_or_none(Usuario.id == carrinho.usuario_id)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    new_carrinho = Carrinho.create(
        usuario=usuario,
        produto_id=carrinho.produto_id,
        tipo_produto=carrinho.tipo_produto,
        quantidade=carrinho.quantidade
    )
    return new_carrinho

@router.put('/{carrinho_id}', response_model=CarrinhoRead)
def update_carrinho(carrinho_id: int, carrinho_data: CarrinhoUpdate):
    carrinho = Carrinho.get_or_none(Carrinho.id == carrinho_id)

    if not carrinho:
        raise HTTPException(status_code=404, detail="Carrinho não encontrado")

    carrinho.usuario = carrinho_data.usuario_id or carrinho.usuario
    carrinho.produto_id = carrinho_data.produto_id or carrinho.produto_id
    carrinho.tipo_produto = carrinho_data.tipo_produto or carrinho.tipo_produto
    carrinho.quantidade = carrinho_data.quantidade or carrinho.quantidade
    carrinho.save()

    return carrinho

@router.delete('/{carrinho_id}', response_model=dict)
def delete_carrinho(carrinho_id: int):
    carrinho = Carrinho.get_or_none(Carrinho.id == carrinho_id)

    if not carrinho:
        raise HTTPException(status_code=404, detail="Carrinho não encontrado")

    carrinho.delete_instance()
    return {"message": "Carrinho deletado com sucesso"}

@router.get('/', response_model=list[CarrinhoRead])
def get_all_carrinhos():
    carrinhos = Carrinho.select()
    return list(carrinhos)

@router.get('/{carrinho_id}', response_model=CarrinhoRead)
def get_carrinho_by_id(carrinho_id: int):
    carrinho = Carrinho.get_or_none(Carrinho.id == carrinho_id)

    if not carrinho:
        raise HTTPException(status_code=404, detail="Carrinho não encontrado")

    return carrinho
