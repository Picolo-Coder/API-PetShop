from peewee import AutoField, CharField, IntegerField, TextField, BooleanField, Model
from config.database import database

class Doacao(Model):
    id = AutoField()
    nome_animal = CharField(max_length=100)
    idade = IntegerField()
    porte = CharField(max_length=10)  # Usando CharField para porte
    sexo = CharField(max_length=10)   # Usando CharField para sexo
    descricao = TextField(null=True)
    castrado = BooleanField(default=False)
    motivo_doacao = TextField(null=True)
    imagem = CharField(max_length=50)

    class Meta:
        database = database
