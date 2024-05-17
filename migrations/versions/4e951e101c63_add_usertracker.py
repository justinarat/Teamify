"""Add UserTracker

Revision ID: 4e951e101c63
Revises: 34900945dd70
Create Date: 2024-05-10 15:06:04.748979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e951e101c63'
down_revision = '34900945dd70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('UserTracker',
    sa.Column('RowID', sa.Text(), nullable=False),
    sa.Column('LobbyID', sa.Text(), nullable=False),
    sa.Column('UserID', sa.Text(), nullable=False),
    sa.Column('Action', sa.Text(), nullable=False),
    sa.Column('Desc', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['LobbyID'], ['Lobby.LobbyID'], ),
    sa.ForeignKeyConstraint(['UserID'], ['Users.UID'], ),
    sa.PrimaryKeyConstraint('RowID'),
    sa.UniqueConstraint('RowID')
    )
    with op.batch_alter_table('Lobby', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyID', sa.Text(), nullable=False))
        batch_op.add_column(sa.Column('GameID', sa.Text(), nullable=False))
        batch_op.create_unique_constraint(None, ['LobbyID'])
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'Games', ['GameID'], ['UID'])
        batch_op.drop_column('LobbyId')
        batch_op.drop_column('GameId')

    with op.batch_alter_table('LobbyPlayers', schema=None) as batch_op:
        batch_op.alter_column('RowID',
               existing_type=sa.NullType(),
               nullable=False)
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'Lobby', ['LobbyID'], ['LobbyID'])

    with op.batch_alter_table('LobbyTags', schema=None) as batch_op:
        batch_op.alter_column('RowID',
               existing_type=sa.NullType(),
               nullable=False)
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'Lobby', ['LobbyID'], ['LobbyID'])

    with op.batch_alter_table('LobbyTimes', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['Repeat'])
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'Lobby', ['LobbyID'], ['LobbyID'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('LobbyTimes', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'Lobby', ['LobbyID'], ['LobbyId'])
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('LobbyTags', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'Lobby', ['LobbyID'], ['LobbyId'])
        batch_op.alter_column('RowID',
               existing_type=sa.NullType(),
               nullable=True)

    with op.batch_alter_table('LobbyPlayers', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'Lobby', ['LobbyID'], ['LobbyId'])
        batch_op.alter_column('RowID',
               existing_type=sa.NullType(),
               nullable=True)

    with op.batch_alter_table('Lobby', schema=None) as batch_op:
        batch_op.add_column(sa.Column('GameId', sa.TEXT(), server_default=sa.text('0'), nullable=False))
        batch_op.add_column(sa.Column('LobbyId', sa.TEXT(), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'Games', ['GameId'], ['UID'])
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('GameID')
        batch_op.drop_column('LobbyID')

    op.drop_table('UserTracker')
    # ### end Alembic commands ###
