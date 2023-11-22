"""empty message

Revision ID: b07f08c347f4
Revises: ecbc3458196c
Create Date: 2023-11-22 09:04:11.011287

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b07f08c347f4'
down_revision: Union[str, None] = 'ecbc3458196c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('connection', sa.Column('company_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'connection', 'company', ['company_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'connection', type_='foreignkey')
    op.drop_column('connection', 'company_id')
    # ### end Alembic commands ###
