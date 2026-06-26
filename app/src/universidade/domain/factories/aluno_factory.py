from src.universidade.domain.entidades.aluno.aluno import Aluno
from src.universidade.domain.entidades.aluno.aluno_intercambio import AlunoIntercambio
from src.universidade.domain.entidades.aluno.aluno_graduacao import AlunoGraduacao
from src.universidade.domain.entidades.aluno.aluno_pos_graduacao import AlunoPosGraduacao


class AlunoFactory:
    def criar_aluno(self, nome, matricula, tipo_aluno) -> Aluno:
        if tipo_aluno == "GRADUACAO":
            return AlunoGraduacao(
                nome,
                matricula,
                tipo_aluno
            )

        if tipo_aluno == "INTERCAMBIO":
            return AlunoIntercambio(
                nome,
                matricula,
                tipo_aluno
            )

        if tipo_aluno == "POSGRADUACAO":
            return AlunoPosGraduacao(
                nome,
                matricula,
                tipo_aluno
            )

        raise ValueError("Tipo inválido")
