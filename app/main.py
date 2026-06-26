from container import create_matricular_aluno


def main():
    use_case = create_matricular_aluno()
    use_case.matricular_aluno(nome="Edy", matricula=888, tipo="GRADUACAO")
    print(f"Aluno Matriculado com Sucesso!")
    aluno = use_case.consultar_matricula(matricula=888)
    print(f"Aluno Consultado com Sucesso - Nome: {aluno.nome}, Matricula: {aluno.matricula}")

main()