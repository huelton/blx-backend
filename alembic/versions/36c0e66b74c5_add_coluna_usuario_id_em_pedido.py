"""Add coluna usuario_id em pedido

Revision ID: 36c0e66b74c5
Revises: afa19c0d9212
Create Date: 2023-01-09 13:07:24.722525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36c0e66b74c5'
down_revision = 'afa19c0d9212'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.drop_column('usuario_id')

    # ### end Alembic commands ###
