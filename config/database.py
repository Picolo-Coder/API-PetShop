from peewee import SqliteDatabase

DATABASE_PATH = 'petshop.db'

database = SqliteDatabase(DATABASE_PATH)

def startup_db():
    from models.usuario import Usuario
    from models.banhotosa import BanhoTosa
    from models.carrinho import Carrinho
    from models.doacao import Doacao
    from models.produtos import Produto
    from models.tipos import Tipo

    database.connect()
    database.create_tables([Usuario, BanhoTosa, Carrinho, Doacao, Produto, Tipo])

def shutdown_db():
    if not database.is_closed():
        database.close()