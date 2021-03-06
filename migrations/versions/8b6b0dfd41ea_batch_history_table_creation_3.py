"""batch history table creation_3

Revision ID: 8b6b0dfd41ea
Revises: 03949a380153
Create Date: 2021-11-02 21:33:05.445976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b6b0dfd41ea'
down_revision = '03949a380153'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('batch_history', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=32), nullable=True))
        batch_op.drop_column('batch_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('batch_history', schema=None) as batch_op:
        batch_op.add_column(sa.Column('batch_name', sa.VARCHAR(length=32), nullable=True))
        batch_op.drop_column('name')

    # ### end Alembic commands ###
