"""Adiciona data_criacao a VendaPorMes

Revision ID: 5dacc74f7907
Revises: 
Create Date: 2024-11-19 08:50:47.450007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dacc74f7907'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venda_por_mes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data_criacao', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venda_por_mes', schema=None) as batch_op:
        batch_op.drop_column('data_criacao')

    # ### end Alembic commands ###
