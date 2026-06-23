from app.universidade.entidades.aluno.aluno import Aluno
from app.universidade.entidades.aluno.aluno_pos_graduacao import AlunoPosGraduacao
from app.universidade.factory.aluno_factory import AlunoFactory


class AlunoPosGraduacaoFactory(AlunoFactory):
    def criar_aluno(self, nome, matricula) -> Aluno:
        return AlunoPosGraduacao(nome, matricula)