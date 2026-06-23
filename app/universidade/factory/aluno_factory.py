from abc import ABC, abstractmethod
from app.universidade.entidades.aluno.aluno import Aluno


class AlunoFactory(ABC):
    @abstractmethod
    def criar_aluno(self, nome, matricula) -> Aluno:
        pass
