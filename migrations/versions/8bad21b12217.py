from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8bad21b12217'
down_revision = '4e951e101c63'
branch_labels = None
depends_on = None

def upgrade():
    # Rename the column if it exists with an incorrect name
    with op.batch_alter_table('Lobby') as batch_op:
        batch_op.alter_column('LobbyId', new_column_name='LobbyID', existing_type=sa.Text())

def downgrade():
    # Revert the column name if downgrading
    with op.batch_alter_table('Lobby') as batch_op:
        batch_op.alter_column('LobbyID', new_column_name='LobbyId', existing_type=sa.Text())
