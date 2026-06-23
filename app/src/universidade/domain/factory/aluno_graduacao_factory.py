from app.src.universidade.domain.entidades.aluno.aluno import Aluno
from app.src.universidade.domain.entidades.aluno.aluno_graduacao import AlunoGraduacao
from app.src.universidade.domain.factory.aluno_factory import AlunoFactory


class AlunoGraduacaoFactory(AlunoFactory):
    def criar_aluno(self, nome, matricula) -> Aluno:
        return AlunoGraduacao(nome, matricula)

