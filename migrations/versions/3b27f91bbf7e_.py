"""empty message

Revision ID: 3b27f91bbf7e
Revises: 41c66ec00612
Create Date: 2024-05-18 16:50:12.449748

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b27f91bbf7e'
down_revision: Union[str, None] = '41c66ec00612'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('topic', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notes', 'topic')
    # ### end Alembic commands ###
