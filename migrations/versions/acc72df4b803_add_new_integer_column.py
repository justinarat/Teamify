"""Add new integer column

Revision ID: acc72df4b803
Revises: 60538b972799
Create Date: 2024-05-14 23:05:16.102889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acc72df4b803'
down_revision = '60538b972799'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('LobbyPlayers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyId', sa.Text(), nullable=False))
        batch_op.alter_column('RowID',
               existing_type=sa.String(),
               nullable=False)
        batch_op.drop_constraint('AAAA', type_='foreignkey')
        batch_op.create_foreign_key('fk_lobby_players_lobby', 'Lobby', ['LobbyId'], ['LobbyId'])
        batch_op.drop_column('LobbyID')

    with op.batch_alter_table('LobbyTags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyId', sa.Text(), nullable=False))
        batch_op.alter_column('RowID',
               existing_type=sa.String(),
               nullable=False)
        batch_op.drop_constraint('fk_lobby_tags_lobby_old', type_='foreignkey')
        batch_op.create_foreign_key('fk_lobby_tags_lobby', 'Lobby', ['LobbyId'], ['LobbyId'])
        batch_op.drop_column('LobbyID')

    with op.batch_alter_table('LobbyTimes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyId', sa.Text(), nullable=False))
        batch_op.create_unique_constraint('LobbyTimesNONULL', ['Repeat'])
        batch_op.drop_constraint('fk_lobby_times_lobby_old', type_='foreignkey')
        batch_op.create_foreign_key('fk_lobby_times_lobby', 'Lobby', ['LobbyId'], ['LobbyId'])
        batch_op.drop_column('LobbyID')

    with op.batch_alter_table('Tags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('TagGroup', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('Suggestion', sa.Integer(), nullable=True))

    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('IsAdmin', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_column('IsAdmin')

    with op.batch_alter_table('Tags', schema=None) as batch_op:
        batch_op.drop_column('Suggestion')
        batch_op.drop_column('TagGroup')

    with op.batch_alter_table('LobbyTimes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyID', sa.TEXT(), server_default=sa.text('0'), nullable=False))
        batch_op.drop_constraint('fk_lobby_times_lobby', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Lobby', ['LobbyID'], ['LobbyId'])
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('LobbyId')

    with op.batch_alter_table('LobbyTags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyID', sa.TEXT(), nullable=False))
        batch_op.drop_constraint('fk_lobby_tags_lobby', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Lobby', ['LobbyID'], ['LobbyId'])
        batch_op.alter_column('RowID',
               existing_type=sa.String(),
               nullable=True)
        batch_op.drop_column('LobbyId')

    with op.batch_alter_table('LobbyPlayers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyID', sa.TEXT(), nullable=False))
        batch_op.drop_constraint('fk_lobby_players_lobby', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Lobby', ['LobbyID'], ['LobbyId'])
        batch_op.alter_column('RowID',
               existing_type=sa.String(),
               nullable=True)
        batch_op.drop_column('LobbyId')

    # ### end Alembic commands ###
