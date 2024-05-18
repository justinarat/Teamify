"""Fix LobbyID column name

Revision ID: 5b8952c80c80
Revises: 8bad21b12217
Create Date: 2024-05-14 16:11:38.561874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b8952c80c80'
down_revision = '8bad21b12217'
branch_labels = None
depends_on = None


def upgrade():
    # Renaming columns or other complex operations
    op.alter_column('Lobby', 'LobbyID', new_column_name='LobbyId')
    # Ensure foreign keys are updated if needed
    op.alter_column('UserTracker', 'LobbyID', new_column_name='LobbyId')

def downgrade():
    # Revert column names if downgrading
    op.alter_column('Lobby', 'LobbyId', new_column_name='LobbyID')
    op.alter_column('UserTracker', 'LobbyId', new_column_name='LobbyID')

