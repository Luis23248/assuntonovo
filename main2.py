import os

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker,declarative_base

db = create_engine("sqlite:///banquinho.db")


Session = sessionmaker(bind = db)
session = Session()

Base = declarative_base()



class Aluno(Base):
    __tablename__ = "Alunos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    ra = Column("R.A.", String)
    nome = Column("Nome", String)
    idade = Column("Idade", Integer)
    email = Column("E-mail", String)




    def __init__(self, ra: str, nome: str, idade: int, email: str):
        self.ra = ra
        self.nome = nome
        self.idade = idade
        self.email = email



Base.metadata.create_all(bind = db)

for i in range(1):
    ra  = input("Digite sua R.A. : ")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    email = input("Digite seu email: ")

aluno = Aluno(nome=nome, ra=ra, idade=idade, email=email)
session.add(aluno)
session.commit()


lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.id} - {aluno.ra} - {aluno.nome} - {aluno.idade} - {aluno.email}")