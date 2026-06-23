from app.universidade.entidades.aluno.aluno import Aluno
from app.universidade.entidades.aluno.aluno_graduacao import AlunoGraduacao
from app.universidade.factory.aluno_factory import AlunoFactory


class AlunoGraduacaoFactory(AlunoFactory):
    def criar_aluno(self, nome, matricula) -> Aluno:
        return AlunoGraduacao(nome, matricula)

