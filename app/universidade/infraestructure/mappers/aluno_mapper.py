from universidade.domain.entidades.aluno.aluno import Aluno
from universidade.infraestructure.database.models.aluno_model import AlunoModel


class AlunoMapper:
    @staticmethod
    def to_model(aluno: Aluno):
        return AlunoModel(
            nome=aluno.nome,
            matricula=aluno.matricula,
            tipo_aluno=aluno.tipo_aluno
        )