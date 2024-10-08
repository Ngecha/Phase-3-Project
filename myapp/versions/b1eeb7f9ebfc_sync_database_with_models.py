"""Sync database with models

Revision ID: b1eeb7f9ebfc
Revises: 7ddc58facf94
Create Date: 2024-09-20 08:39:47.680607

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1eeb7f9ebfc'
down_revision: Union[str, None] = '7ddc58facf94'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('circuit_id', sa.String(), nullable=True),
    sa.Column('team_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['circuit_id'], ['circuits.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###
