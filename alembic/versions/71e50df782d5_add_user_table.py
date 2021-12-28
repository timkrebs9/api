"""add user table

Revision ID: 71e50df782d5
Revises: 9c22fcdcdac7
Create Date: 2021-12-28 16:54:06.559137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71e50df782d5'
down_revision = '9c22fcdcdac7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass