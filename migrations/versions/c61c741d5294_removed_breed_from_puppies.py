"""removed breed from puppies

Revision ID: c61c741d5294
Revises: 5f6405cf0910
Create Date: 2018-10-05 00:56:46.978251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c61c741d5294'
down_revision = '5f6405cf0910'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('puppies', 'breed')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('puppies', sa.Column('breed', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###
