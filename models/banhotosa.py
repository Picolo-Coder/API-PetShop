from peewee import AutoField, CharField, DateTimeField, ForeignKeyField, Model
from config.database import database
from models.usuario import Usuario  # Supondo que você tenha um modelo Usuario

class BanhoTosa(Model):
    id = AutoField()
    usuario = ForeignKeyField(Usuario, backref='banhos_tosas')
    tipo_servico = CharField(choices=['banho', 'tosa', 'banho_tosa'])  # Use CharField com opções
    data_reserva = DateTimeField()

    class Meta:
        database = database

    def save(self, *args, **kwargs):
        # Valida o campo tipo_servico antes de salvar
        if self.tipo_servico not in ['banho', 'tosa', 'banho_tosa']:
            raise ValueError('Tipo de serviço inválido.')
        return super().save(*args, **kwargs)