from universidade.infraestructure.database.session import SessionLocal
from universidade.infraestructure.database.repositories.aluno_repository_sqlalchemy import AlunoRepositorySqlAlchemy
from universidade.application.use_cases.matricular_aluno import MatricularAlunoUseCase
from universidade.domain.factories.aluno_factory import AlunoFactory


def create_matricular_aluno():
    session = SessionLocal()
    repository = AlunoRepositorySqlAlchemy(session)
    factory = AlunoFactory()
    return MatricularAlunoUseCase(factory, repository)