"""stu_wor_id attribute is added

Revision ID: ea3313043bf2
Revises: 
Create Date: 2021-04-02 12:45:14.122509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea3313043bf2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('stu_wor_id', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_users_stu_wor_id'), 'users', ['stu_wor_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_stu_wor_id'), table_name='users')
    op.drop_column('users', 'stu_wor_id')
    # ### end Alembic commands ###
