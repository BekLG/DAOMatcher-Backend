"""refactor: Changed username to non unique

Revision ID: 3292a1bedfac
Revises: 2d4b62e5eaba
Create Date: 2024-04-18 09:11:20.889722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3292a1bedfac'
down_revision = '2d4b62e5eaba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('display_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('display_name', ['display_name'], unique=True)

    # ### end Alembic commands ###
