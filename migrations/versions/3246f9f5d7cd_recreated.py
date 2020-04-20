"""recreated

Revision ID: 3246f9f5d7cd
Revises: 
Create Date: 2020-03-29 21:20:14.891861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3246f9f5d7cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie', sa.String(length=80), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('votes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movies_date'), 'movies', ['date'], unique=False)
    op.create_index(op.f('ix_movies_username'), 'movies', ['username'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_movies_username'), table_name='movies')
    op.drop_index(op.f('ix_movies_date'), table_name='movies')
    op.drop_table('movies')
    # ### end Alembic commands ###
