from dataclasses import dataclass


@dataclass
class Disciplina:
    nome: str
    id_curso: int
    carga_horaria: str
    professor: str
