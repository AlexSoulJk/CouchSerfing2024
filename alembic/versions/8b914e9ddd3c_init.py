"""init

Revision ID: 8b914e9ddd3c
Revises: 
Create Date: 2024-02-22 00:40:30.852228

"""
from typing import Sequence, Union

import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b914e9ddd3c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=100), nullable=True),
    sa.Column('date_start', sa.Date(), nullable=False),
    sa.Column('login', sqlalchemy_utils.types.encrypted.encrypted_type.StringEncryptedType(length=100), nullable=False),
    sa.Column('password', sqlalchemy_utils.types.encrypted.encrypted_type.StringEncryptedType(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
