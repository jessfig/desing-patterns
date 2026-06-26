from app.src.universidade.infraestructure.database.session import SessionLocal
from app.src.universidade.infraestructure.database.repositories.aluno_repository_sqlalchemy import AlunoRepositorySqlAlchemy
from app.src.universidade.application.use_cases.matricular_aluno import MatricularAlunoUseCase
from app.src.universidade.domain.factories.aluno_factory import AlunoFactory


def main():
    session = SessionLocal()
    repository = AlunoRepositorySqlAlchemy(session)
    factory = AlunoFactory()
    use_case = MatricularAlunoUseCase(factory, repository)
    use_case.matricular_aluno(nome="Edy", matricula=888, tipo="GRADUACAO")
    aluno = use_case.consultar_matricula(matricula=888)
    print(f"Nome: {aluno.nome}, Matricula: {aluno.matricula}")

main()