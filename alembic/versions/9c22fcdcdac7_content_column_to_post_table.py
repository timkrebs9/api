"""content column to post table

Revision ID: 9c22fcdcdac7
Revises: db3e82101d29
Create Date: 2021-12-28 15:02:21.583920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c22fcdcdac7'
down_revision = 'db3e82101d29'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
