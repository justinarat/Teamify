"""we do this MANUALLY

Revision ID: e669d5773da2
Revises: 7d1d35941892
Create Date: 2024-05-19 02:21:13.771855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e669d5773da2'
down_revision = '7d1d35941892'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    # Rename the column
    op.alter_column('LobbyTimes', 'Repeat', new_column_name='DayOfWeek')
    with op.batch_alter_table('Lobby', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Name', sa.TEXT(), nullable=True))


def downgrade():
    # Revert the column name
    op.alter_column('LobbyTimes', 'DayOfWeek', new_column_name='Repeat')
    with op.batch_alter_table('Lobby', schema=None) as batch_op:
        batch_op.drop_column('Name')


