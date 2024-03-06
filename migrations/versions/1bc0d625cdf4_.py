"""empty message

Revision ID: 1bc0d625cdf4
Revises: 
Create Date: 2024-03-06 12:39:52.891159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bc0d625cdf4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('memes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_path', sa.String(length=255), nullable=False),
    sa.Column('text', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('memes')
    # ### end Alembic commands ###
