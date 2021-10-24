"""20211023 model update

Revision ID: 90e6ceda6f2c
Revises: c9d29fb90bd4
Create Date: 2021-10-24 00:09:34.912546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90e6ceda6f2c'
down_revision = 'c9d29fb90bd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('containertypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('volume_max', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('containers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('batch_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('volume_actual', sa.Float(), nullable=True),
    sa.Column('is_vessel', sa.Boolean(), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['batch_id'], ['batches.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['statuses.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['containertypes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('statuses', sa.Column('type', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('statuses', 'type')
    op.drop_table('containers')
    op.drop_table('locations')
    op.drop_table('containertypes')
    # ### end Alembic commands ###
