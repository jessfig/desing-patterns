"""create alunos table

Revision ID: e818f2f6df07
Revises: 
Create Date: 2026-06-24 12:00:57.448135

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e818f2f6df07'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "alunos",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True
        ),
        sa.Column(
            "nome",
            sa.String(100),
            nullable=False
        ),
        sa.Column(
            "matricula",
            sa.Integer(),
            nullable=False,
            unique=True
        ),
        sa.Column(
            "tipo_aluno",
            sa.String(12),
            nullable=False
        ),
        sa.CheckConstraint(
            "tipo_aluno IN ('GRADUACAO', 'INTERCAMBIO', 'POSGRADUACAO')",
            name="ck_tipo_aluno"
        )
    )

def downgrade():
    op.drop_table("alunos")
