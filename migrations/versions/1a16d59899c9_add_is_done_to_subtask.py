"""Add is_done to SubTask

Revision ID: 1a16d59899c9
Revises: c2abbb198d94
Create Date: 2024-07-23 21:04:41.111807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a16d59899c9'
down_revision = 'c2abbb198d94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sub_task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_done', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sub_task', schema=None) as batch_op:
        batch_op.drop_column('is_done')

    # ### end Alembic commands ###
