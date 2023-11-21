"""empty message

Revision ID: 485e880b3642
Revises: dc2bebcb7e71
Create Date: 2023-11-21 20:29:54.378534

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '485e880b3642'
down_revision: Union[str, None] = 'dc2bebcb7e71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('name', sa.String(length=127), nullable=True),
    sa.Column('measure', sa.String(length=15), nullable=True),
    sa.Column('code', sa.String(length=31), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('season_products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('season', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('season_products')
    op.drop_table('products')
    # ### end Alembic commands ###