from peewee import AutoField, CharField, DecimalField, TextField, ForeignKeyField, Model
from config.database import database
from models.tipos import Tipo  # Supondo que você tenha um modelo Tipo

class Produto(Model):
    id = AutoField()
    nome = CharField(max_length=100)  # Defina um comprimento máximo para garantir integridade
    preco = DecimalField(max_digits=10, decimal_places=2)
    descricao = TextField(null=True)  # Texto opcional
    volume = TextField(null=True)  # Texto opcional
    imagem = CharField(max_length=255)  # Defina um comprimento máximo para URLs ou caminhos
    tipo = ForeignKeyField(Tipo, backref='produtos')

    class Meta:
        database = database

    def save(self, *args, **kwargs):
        # Valida o campo nome antes de salvar
        if not self.nome:
            raise ValueError('O nome do produto não pode estar vazio.')
        return super().save(*args, **kwargs)