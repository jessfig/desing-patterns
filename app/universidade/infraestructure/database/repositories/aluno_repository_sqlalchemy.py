from universidade.infraestructure.database.repositories.aluno_repository import AlunoRepository
from universidade.infraestructure.database.models.aluno_model import AlunoModel
from universidade.domain.entidades.aluno.aluno import Aluno
from universidade.infraestructure.mappers.aluno_mapper import AlunoMapper


class AlunoRepositorySqlAlchemy(AlunoRepository):
    def __init__(self, session):
        self._session = session

    def salvar(self, aluno: Aluno):
        model = AlunoMapper.to_model(aluno)
        self._session.add(model)
        self._session.commit()
        print('Aluno salvo com sucesso no banco de dados')

    def buscar_por_matricula(self, matricula):
        return self._session.query(AlunoModel).filter_by(matricula=matricula).first()
