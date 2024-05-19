"""add Max Players To Lobby

Revision ID: f4a8511bee5a
Revises: 920393e46801
Create Date: 2024-05-18 21:58:27.843933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4a8511bee5a'
down_revision = '920393e46801'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Lobby', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyID', sa.Text(), nullable=False))
        batch_op.add_column(sa.Column('maxPlayers', sa.Integer(), nullable=True))
        batch_op.create_unique_constraint('uq_lobby_lobbyid', ['LobbyID'])
        batch_op.drop_column('LobbyId')

    with op.batch_alter_table('LobbyPlayers', schema=None) as batch_op:
        batch_op.alter_column('RowID',
               existing_type=sa.NullType(),
               nullable=False)
        batch_op.drop_constraint('fk_lobby_players_lobby', type_='foreignkey')
        batch_op.create_foreign_key('fk_lobby_players_lobby', 'Lobby', ['LobbyID'], ['LobbyID'])

    with op.batch_alter_table('LobbyTags', schema=None) as batch_op:
        batch_op.alter_column('RowID',
               existing_type=sa.NullType(),
               nullable=False)
        batch_op.drop_constraint('fk_lobby_tags_lobby', type_='foreignkey')
        batch_op.create_foreign_key('fk_lobby_tags_lobby', 'Lobby', ['LobbyID'], ['LobbyID'])

    with op.batch_alter_table('LobbyTimes', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_lobby_times_repeat', ['RowID'])
        batch_op.drop_constraint('fk_lobby_times_lobby', type_='foreignkey')
        batch_op.create_foreign_key('fk_lobby_times_lobby', 'Lobby', ['LobbyID'], ['LobbyID'])

    with op.batch_alter_table('UserTracker', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyID', sa.Text(), nullable=False))
        batch_op.drop_constraint('fk_user_tracker_lobby', type_='foreignkey')
        batch_op.create_foreign_key('fk_user_tracker_lobby', 'Lobby', ['LobbyID'], ['LobbyID'])
        batch_op.drop_column('LobbyId')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('UserTracker', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyId', sa.TEXT(), nullable=False))
        batch_op.drop_constraint('fk_user_tracker_lobby', type_='foreignkey')
        batch_op.create_foreign_key('fk_user_tracker_lobby', 'Lobby', ['LobbyId'], ['LobbyId'])
        batch_op.drop_column('LobbyID')

    with op.batch_alter_table('LobbyTimes', schema=None) as batch_op:
        batch_op.drop_constraint('fk_lobby_times_lobby', type_='foreignkey')
        batch_op.create_foreign_key('fk_lobby_times_lobby', 'Lobby', ['LobbyID'], ['LobbyId'])
        batch_op.drop_constraint('uq_lobby_times_repeat', type_='unique')

    with op.batch_alter_table('LobbyTags', schema=None) as batch_op:
        batch_op.drop_constraint('fk_lobby_tags_lobby', type_='foreignkey')
        batch_op.create_foreign_key('fk_lobby_tags_lobby', 'Lobby', ['LobbyID'], ['LobbyId'])
        batch_op.alter_column('RowID',
               existing_type=sa.NullType(),
               nullable=True)

    with op.batch_alter_table('LobbyPlayers', schema=None) as batch_op:
        batch_op.drop_constraint('fk_lobby_players_lobby', type_='foreignkey')
        batch_op.create_foreign_key('fk_lobby_players_lobby', 'Lobby', ['LobbyID'], ['LobbyId'])
        batch_op.alter_column('RowID',
               existing_type=sa.NullType(),
               nullable=True)

    with op.batch_alter_table('Lobby', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyId', sa.TEXT(), nullable=False))
        batch_op.drop_constraint('uq_lobby_lobbyid', type_='unique')
        batch_op.drop_column('maxPlayers')
        batch_op.drop_column('LobbyID')

    # ### end Alembic commands ###
