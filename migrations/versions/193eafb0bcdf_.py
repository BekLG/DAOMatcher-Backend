"""empty message

Revision ID: 193eafb0bcdf
Revises: 2d4b62e5eaba
Create Date: 2024-04-29 15:00:42.904862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '193eafb0bcdf'
down_revision = '2d4b62e5eaba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_setting',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('default_user_count', sa.Integer(), nullable=False),
    sa.Column('default_depth_count', sa.Integer(), nullable=False),
    sa.Column('theme', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_usage',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('token_count', sa.Integer(), nullable=False),
    sa.Column('search_count', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('username',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.Column('display_name', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('password_salt', sa.String(length=100), nullable=False),
    sa.Column('api_key', sa.String(length=50), nullable=True),
    sa.Column('user_setting_id', sa.String(length=50), nullable=True),
    sa.Column('usage_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['usage_id'], ['user_usage.id'], ),
    sa.ForeignKeyConstraint(['user_setting_id'], ['user_setting.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('display_name'),
    sa.UniqueConstraint('email')
    )
    op.create_table('search_result',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('time_stamp', sa.DateTime(), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('user_id', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('search_usernames',
    sa.Column('search_id', sa.String(length=50), nullable=False),
    sa.Column('username_id', sa.String(length=50), nullable=False),
    sa.Column('type', sa.Enum('SEED', 'FOUND', name='usernametype'), nullable=True),
    sa.ForeignKeyConstraint(['search_id'], ['search_result.id'], ),
    sa.ForeignKeyConstraint(['username_id'], ['username.id'], ),
    sa.PrimaryKeyConstraint('search_id', 'username_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('search_usernames')
    op.drop_table('search_result')
    op.drop_table('user')
    op.drop_table('username')
    op.drop_table('user_usage')
    op.drop_table('user_setting')
    # ### end Alembic commands ###
