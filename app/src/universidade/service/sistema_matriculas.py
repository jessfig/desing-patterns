from app.src.universidade.domain.factory.aluno_factory import AlunoFactory


class SistemaMatriculas:
    def __init__(self, factory: AlunoFactory):
        self.__aluno_factory = factory

    def matricular_aluno(self, nome, matricula):
        return self.__aluno_factory.criar_aluno(nome, matricula)
