import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker,declarative_base


# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")


# Conexão com o banco de dados.
Session = sessionmaker(bind = db)
session = Session()


# I/O
# I = input (Entrada)
# O = output (Saída)

# Abrindo uma conexão



# Criando tabela.
Base = declarative_base()

class Usuario(Base):
    # Definindo nome da tabela.
    __tablename__ = "usuarios"


    # Definindo atributos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    

    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str):

        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

# Salvar no banco de dados.
# usuario = Usuario("Marta", "email@hotmail.com", "123")
usuario = Usuario(nome="LPL", email="Email", senha="123")
session.add(usuario)
session.commit()


# Mostrando conteudo do banco de dados.
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")