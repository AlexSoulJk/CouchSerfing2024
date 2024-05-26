"""change possible interests

Revision ID: 1fb20c67d85c
Revises: dee8bafa78de
Create Date: 2024-05-20 19:21:14.313781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1fb20c67d85c'
down_revision: Union[str, None] = 'dee8bafa78de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questionroomrules',
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answerrules',
    sa.Column('rule_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['rule_id'], ['rules.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('questionrules', sa.Column('description', sa.String(length=100), nullable=False))
    op.drop_column('questionrules', 'description_interest')
    op.drop_column('questionrules', 'description_rule')
    op.add_column('rules', sa.Column('quest_id', sa.Integer(), nullable=True))
    op.drop_constraint('rules_room_rule_id_fkey', 'rules', type_='foreignkey')
    op.create_foreign_key(None, 'rules', 'questionroomrules', ['quest_id'], ['id'])
    op.drop_column('rules', 'room_rule_id')
    op.drop_column('rules', 'description_interest')
    op.drop_column('rules', 'description_rule')
    op.drop_constraint('useranswerrules_answer_id_fkey', 'useranswerrules', type_='foreignkey')
    op.create_foreign_key(None, 'useranswerrules', 'answerrules', ['answer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'useranswerrules', type_='foreignkey')
    op.create_foreign_key('useranswerrules_answer_id_fkey', 'useranswerrules', 'rules', ['answer_id'], ['id'])
    op.add_column('rules', sa.Column('description_rule', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('rules', sa.Column('description_interest', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('rules', sa.Column('room_rule_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'rules', type_='foreignkey')
    op.create_foreign_key('rules_room_rule_id_fkey', 'rules', 'questionrules', ['room_rule_id'], ['id'])
    op.drop_column('rules', 'description')
    op.drop_column('rules', 'quest_id')
    op.add_column('questionrules', sa.Column('description_rule', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('questionrules', sa.Column('description_interest', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_column('questionrules', 'description')
    op.drop_table('answerrules')
    op.drop_table('questionroomrules')
    # ### end Alembic commands ###
