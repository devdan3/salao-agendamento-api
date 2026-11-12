from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ClienteCreate(BaseModel):
    nome_cliente: str
    telefone_cliente: str

class ServicoCreate(BaseModel):
    nome_servico: str
    preco_servico: float
    descricao: str | None = None
    duracao: int

class ProfissionalCreate(BaseModel):
    nome_profissional: str
    telefone_profissional: str

class ClienteResponse(ClienteCreate):
    id_cliente: int
    model_config = ConfigDict(from_attributes=True)

class ServicoResponse(ServicoCreate):
    id_servico: int
    model_config = ConfigDict(from_attributes=True)

class ProfissionalResponse(ProfissionalCreate):
    id_profissional: int
    model_config = ConfigDict(from_attributes=True)

class AgendamentoCreate(BaseModel):
    id_cliente: int
    id_servico: int
    id_profissional: int
    inicio_agendamento: datetime 
