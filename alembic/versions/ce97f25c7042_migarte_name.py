"""migarte name

Revision ID: ce97f25c7042
Revises: 6788b37a21a3
Create Date: 2023-11-20 23:02:37.916251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ce97f25c7042'
down_revision: Union[str, None] = '6788b37a21a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=31), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###