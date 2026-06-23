from app.src.universidade.domain.entidades.aluno.aluno import Aluno
from app.src.universidade.domain.entidades.aluno.aluno_intercambio import AlunoIntercambio
from app.src.universidade.domain.factory.aluno_factory import AlunoFactory


class AlunoIntercambioFactory(AlunoFactory):
    def criar_aluno(self, nome, matricula) -> Aluno:
        return AlunoIntercambio(nome, matricula)