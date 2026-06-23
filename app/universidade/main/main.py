from app.universidade.factory.aluno_graduacao_factory import AlunoGraduacaoFactory
from app.universidade.factory.aluno_intercambio_factory import AlunoIntercambioFactory
from app.universidade.service.sistema_matriculas import SistemaMatriculas


def main():
    aluno_graduacao_factory = AlunoGraduacaoFactory()
    matricular = SistemaMatriculas(aluno_graduacao_factory)
    aluno_matriculado = matricular.matricular_aluno('Jessica', 123)
    print(f'Aluno matriculado com sucesso! Nome: {aluno_matriculado.nome}, Matricula: {aluno_matriculado.matricula}')

    aluno_intercambio_factory = AlunoIntercambioFactory()
    matricular = SistemaMatriculas(aluno_intercambio_factory)
    aluno_matriculado = matricular.matricular_aluno('Maria', 456)
    print(f'Aluno matriculado com sucesso! Nome: {aluno_matriculado.nome}, Matricula: {aluno_matriculado.matricula}')

main()