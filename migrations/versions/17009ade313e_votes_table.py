"""Votes Table

Revision ID: 17009ade313e
Revises: fe12caf47c33
Create Date: 2020-04-20 17:42:33.565790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17009ade313e'
down_revision = 'fe12caf47c33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('votes', sa.Column('category', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('votes', 'category')
    # ### end Alembic commands ###
