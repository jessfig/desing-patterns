# Universidade - Desing Patterns 
Projeto criado para realizar a revisão de desing patterns.

## Tecnologias utilizadas
- Python
- PostgreSQL
- Docker
- SQLAlchemy
- Alembic

## Arquitetura
- Clean Architecture

## Patterns implementados
- Factory
- Repository
- Mapper

## Como executar o projeto:
  - py -m pip install -r requirements.txt
  - cp .env.example .env 
  - docker compose up -d 
  - py -m alembic upgrade head 
  - python app/main.py