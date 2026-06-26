from src.universidade.domain.factories.aluno_factory import AlunoFactory
from src.universidade.infraestructure.database.repositories.aluno_repository import AlunoRepository


class MatricularAlunoUseCase:
    def __init__(self, factory: AlunoFactory, repository: AlunoRepository):
        self.__aluno_factory = factory
        self.__repository = repository

    def matricular_aluno(self, nome, matricula, tipo):
        aluno = self.__aluno_factory.criar_aluno(nome, matricula, tipo)
        self.__repository.salvar(aluno)
        return aluno

    def consultar_matricula(self, matricula):
        return self.__repository.buscar_por_matricula(matricula)
