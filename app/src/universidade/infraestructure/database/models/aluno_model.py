from sqlalchemy import Column, Integer, String
from src.universidade.infraestructure.database.base import Base


class AlunoModel(Base):
    __tablename__ = "alunos"

    id = Column(
        Integer,
        primary_key=True
    )

    nome = Column(
        String(100)
    )

    matricula = Column(
        Integer,
        unique=True
    )

    tipo_aluno = Column(
        String(12)
    )