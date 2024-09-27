from peewee import AutoField, CharField, Model
from config.database import database

class Tipo(Model):
    id = AutoField()
    nome_tipo = CharField(max_length=50, unique=True)  # Adiciona comprimento máximo e garante unicidade

    class Meta:
        database = database
        table_name = 'tipos'  # Define explicitamente o nome da tabela no banco de dados

    def __str__(self):
        return f'Tipo(id={self.id}, nome_tipo={self.nome_tipo})'
