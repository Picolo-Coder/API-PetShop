from peewee import Model, AutoField, CharField, TextField, DateTimeField, SQL
from config.database import database

class Usuario(Model):
    id = AutoField()
    nome = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    telefone = CharField(max_length=15, null=True)
    senha = CharField(max_length=255)
    cpf = CharField(max_length=11, unique=True)
    tipo_usuario = CharField(max_length=1)  # Assumindo que ENUM é armazenado como CHAR
    data_criacao = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

    class Meta:
        database = database
        table_name = 'usuarios'
