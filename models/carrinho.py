from peewee import AutoField, CharField, ForeignKeyField, IntegerField, Model, TextField
from config.database import database
from models.usuario import Usuario

class Carrinho(Model):
    id = AutoField()
    usuario = ForeignKeyField(Usuario, backref='carrinhos')
    produto_id = IntegerField()
    tipo_produto = CharField(choices=['Camas', 'Casinhas', 'Brinquedos', 'Farmacia', 'Higiene', 'Alimentacao'])
    quantidade = IntegerField(default=1)

    class Meta:
        database = database
