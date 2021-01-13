"""empty message

Revision ID: a82035ce768d
Revises: 
Create Date: 2021-01-13 12:06:29.886232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a82035ce768d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userstbl',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('api_key', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('email_address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'api_key', 'username'),
    sa.UniqueConstraint('api_key'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userstbl')
    # ### end Alembic commands ###
