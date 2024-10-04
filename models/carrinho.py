from peewee import AutoField, ForeignKeyField, IntegerField, Model
from config.database import database
from models.usuario import Usuario
from models.produtos import Produto

class Carrinho(Model):
    id = AutoField()  # Chave primária
    usuario = ForeignKeyField(Usuario, backref='carrinhos', on_delete='CASCADE')  # Referência ao usuário
    produto = ForeignKeyField(Produto, backref='carrinhos', on_delete='CASCADE')  # Referência ao produto
    quantidade = IntegerField(default=1)  # Quantidade do produto

    class Meta:
        database = database
        indexes = (
            (('usuario', 'produto'), True),  # Índice único para evitar duplicatas do mesmo produto por usuário
        )
