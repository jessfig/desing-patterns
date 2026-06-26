from abc import ABC, abstractmethod


class AlunoRepository(ABC):
    @abstractmethod
    def salvar(self, aluno):
        pass

    @abstractmethod
    def buscar_por_matricula(self, matricula):
        pass
