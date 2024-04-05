"""feat: Removed token fields


Revision ID: d3df21070fd4
Revises: 2a0f722bf6b0
Create Date: 2024-03-30 11:43:56.266426

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd3df21070fd4'
down_revision = '2a0f722bf6b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('verification_token')
        batch_op.drop_column('password_reset_token')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_reset_token', mysql.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column('verification_token', mysql.VARCHAR(length=50), nullable=True))

    # ### end Alembic commands ###
