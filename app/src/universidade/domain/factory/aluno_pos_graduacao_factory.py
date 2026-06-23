from app.src.universidade.domain.entidades.aluno.aluno import Aluno
from app.src.universidade.domain.entidades.aluno.aluno_pos_graduacao import AlunoPosGraduacao
from app.src.universidade.domain.factory.aluno_factory import AlunoFactory


class AlunoPosGraduacaoFactory(AlunoFactory):
    def criar_aluno(self, nome, matricula) -> Aluno:
        return AlunoPosGraduacao(nome, matricula)