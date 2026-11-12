from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def raiz():
    return {"status": "ok"}

@app.post("/clientes", response_model=schemas.ClienteResponse, status_code=201)
def criar_cliente(dados: schemas.ClienteCreate, db: Session = Depends(get_db)):
    cliente = models.Cliente(**dados.model_dump())
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

@app.post("/servicos", response_model=schemas.ServicoResponse, status_code=201)
def criar_servico(dados: schemas.ServicoCreate, db: Session = Depends(get_db)):
    servico = models.Servico(**dados.model_dump())
    db.add(servico)
    db.commit()
    db.refresh(servico)
    return servico

@app.post("/profissionais", response_model=schemas.ProfissionalResponse, status_code=201)
def criar_profissional(dados: schemas.ProfissionalCreate, db: Session = Depends(get_db)):
    profissional = models.Profissional(**dados.model_dump())
    db.add(profissional)
    db.commit()
    db.refresh(profissional)
    return profissional