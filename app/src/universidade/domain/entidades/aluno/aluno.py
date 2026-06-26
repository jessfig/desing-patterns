from dataclasses import dataclass


@dataclass
class Aluno:
    nome: str
    matricula: int
    tipo_aluno: str