"""Add new integer column

Revision ID: 920393e46801
Revises: 41ef29e71add
Create Date: 2024-05-14 23:16:11.271825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '920393e46801'
down_revision = '41ef29e71add'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('LobbyPlayers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyId', sa.Text(), nullable=False))
        batch_op.alter_column('RowID',
               existing_type=sa.NullType(),
               nullable=False)
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('fk_lobby_players_lobby', 'Lobby', ['LobbyId'], ['LobbyId'])
        batch_op.drop_column('LobbyID')

    with op.batch_alter_table('LobbyTags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyId', sa.Text(), nullable=False))
        batch_op.alter_column('RowID',
               existing_type=sa.NullType(),
               nullable=False)
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('fk_lobby_tags_lobby', 'Lobby', ['LobbyId'], ['LobbyId'])
        batch_op.drop_column('LobbyID')

    with op.batch_alter_table('LobbyTimes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyId', sa.Text(), nullable=False))
        batch_op.create_unique_constraint(None, ['Repeat'])
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('fk_lobby_times_lobby', 'Lobby', ['LobbyId'], ['LobbyId'])
        batch_op.drop_column('LobbyID')

    with op.batch_alter_table('Tags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('TagGroup', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('Suggestion', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
               existing_type=sa.NullType(),
               nullable=True)
        batch_op.drop_column('LobbyId')

    with op.batch_alter_table('LobbyPlayers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('LobbyID', sa.TEXT(), nullable=False))
        batch_op.drop_constraint('fk_lobby_players_lobby', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Lobby', ['LobbyID'], ['LobbyId'])
        batch_op.alter_column('RowID',
               existing_type=sa.NullType(),
               nullable=True)
        batch_op.drop_column('LobbyId')

    # ### end Alembic commands ###
