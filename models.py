from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from database import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True)
    nome_cliente = Column(String, nullable=False)
    telefone_cliente = Column(String, nullable=False)

class Servico(Base):
    __tablename__ = "servico"

    id_servico = Column(Integer, primary_key=True)
    nome_servico = Column(String, nullable=False)
    preco_servico = Column(Float, nullable=False)
    descricao = Column(String)
    duracao = Column(Integer, nullable=False) 

class Profissional(Base):
    __tablename__ = "profissional"

    id_profissional = Column(Integer, primary_key=True)
    nome_profissional = Column(String, nullable=False)
    telefone_profissional = Column(String, nullable=False)

class Agendamento(Base):
    __tablename__ = "agendamento"

    id_agendamento = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id_cliente"), nullable=False)
    id_servico = Column(Integer, ForeignKey("servico.id_servico"), nullable=False)
    id_profissional = Column(Integer, ForeignKey("profissional.id_profissional"), nullable=False)
    inicio_agendamento = Column(DateTime, nullable=False)
    fim_agendamento = Column(DateTime, nullable=False)
    status_agendamento = Column(String, default="agendado", nullable=False) #concluido, cancelado, agendado