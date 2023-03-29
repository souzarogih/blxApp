from fastapi import FastAPI, Depends, status
from src.schemas.schemas import Produto, ProdutoResponse
from sqlalchemy.orm import Session
from typing import List
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

criar_db()

app = FastAPI()


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoResponse)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


# uvicorn src.server:app --reload --reload-dir=src
# https://github.com/rogeriosilva-ifpi/ifpi-tds-20211-backend/blob/main/blx-backend/src/infra/sqlalchemy/config/database.py
# https://alembic.sqlalchemy.org/en/latest/
# Comando para inicializar o alembic
# $ alembic init alembic

# Criar uma nova migração
# $ alembic revision --autogenerate -m "Inicial"

# Executar migrações
# $ alembic upgrade head

