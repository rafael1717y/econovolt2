"""empty message

Revision ID: dc6c1380a53f
Revises: 
Create Date: 2022-05-14 10:43:57.333516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc6c1380a53f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('simulation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(length=120), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('time_of_use', sa.Integer(), nullable=True),
    sa.Column('potency', sa.Integer(), nullable=True),
    sa.Column('state', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_simulation_item'), 'simulation', ['item'], unique=False)
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('consumption', sa.Integer(), nullable=True),
    sa.Column('tax', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('simulation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['simulation_id'], ['simulation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_result_timestamp'), 'result', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_result_timestamp'), table_name='result')
    op.drop_table('result')
    op.drop_index(op.f('ix_simulation_item'), table_name='simulation')
    op.drop_table('simulation')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###