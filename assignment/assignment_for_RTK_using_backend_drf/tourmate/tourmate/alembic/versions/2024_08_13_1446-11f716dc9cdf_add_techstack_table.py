"""add techstack table

Revision ID: 11f716dc9cdf
Revises: 49de39bd910e
Create Date: 2024-08-13 14:46:16.259958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '11f716dc9cdf'
down_revision: Union[str, None] = '49de39bd910e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None




def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('techstack',
    
    
    sa.Column('name', sa.String(30), nullable=False),
    sa.Column('code', sa.String(10), nullable=True, default='')
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('techstack')
    # ### end Alembic commands ###
