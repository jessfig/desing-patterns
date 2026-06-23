from app.universidade.entidades.aluno.aluno import Aluno
from app.universidade.entidades.aluno.aluno_intercambio import AlunoIntercambio
from app.universidade.factory.aluno_factory import AlunoFactory


class AlunoIntercambioFactory(AlunoFactory):
    def criar_aluno(self, nome, matricula) -> Aluno:
        return AlunoIntercambio(nome, matricula)