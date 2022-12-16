"""empty message

Revision ID: 5a22bf7a20c6
Revises: 1e23e7ec90ed
Create Date: 2022-12-15 12:13:33.184223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a22bf7a20c6'
down_revision = '1e23e7ec90ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('uid', sa.String(length=10), nullable=False),
    sa.Column('url', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uid'),
    sa.UniqueConstraint('url')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('hair_color', sa.String(length=250), nullable=True),
    sa.Column('skin_color', sa.String(length=250), nullable=True),
    sa.Column('eye_color', sa.String(length=250), nullable=True),
    sa.Column('birth_year', sa.String(length=250), nullable=True),
    sa.Column('gender', sa.String(length=250), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    op.drop_table('people')
    op.drop_table('favoritos')
    # ### end Alembic commands ###
