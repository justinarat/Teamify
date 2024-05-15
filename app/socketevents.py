from app import socketio, db
from app.model import LobbyPlayers
from flask import session
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_login import current_user

@socketio.on("connect")
def connect():
    if not "lobby_id" in session:
        socketio.stop()

# Events for players joining or leaving
@socketio.on("player_join")
def player_join():
    """Broadcasts the new player's username to players.
    
    Sent data is in the format:
        data_to_send = {
            "sender_username": "sender_username", 
        }

    Note: this doesn't update the database for adding a player to the lobby.
    This should be done in the lobby_view() function in routes.py.
    """
    lobby_id = session["lobby_id"]
    join_room(lobby_id)
    sender_username = current_user.Username
    data_to_send = {
        "sender_username": sender_username 
    }
    emit("player_join", data_to_send, to=lobby_id)

@socketio.on("player_leave")
def player_leave():
    """Broadcasts the username of the player that left.
    
    Sent data is in the format:
        data_to_send = {
            "sender_username": "sender_username" 
        }
    """
    lobby_id = session["lobby_id"]
    db.session.delete(LobbyPlayers.query.filter_by(LobbyID=lobby_id, userID=current_user.get_id()).first())
    db.session.commit()
    session.pop("lobby_id")
    sender_username = current_user.Username
    leave_room(lobby_id)
    data_to_send = {
        "sender_username": sender_username
    }
    emit("player_leave", data_to_send, to=lobby_id)

@socketio.on("player_kick")
def player_kick(data):
    lobby_id = session["lobby_id"]
    # TODO: Need to figure out how to kick the player so that they can't just
    #       edit the javascript that disconnects them from the lobby
    emit("player_kick", data, to=lobby_id)


# Events all users can send
@socketio.on("player_text")
def player_text(data):
    """Broadcasts the player's username and text message.

    data is in the format:
        data = {
            "body": "text_message"
        }

    Sent data is in the format:
        data_to_send = {
            "sender_username": "sender_username", 
            "body": "text_message"
        }
    """
    lobby_id = session["lobby_id"]
    text_message = data["body"]
    # TODO: Add message to database if needed
    sender_username = current_user.Username
    data_to_send = {
        "sender_username": sender_username, 
        "body": text_message
    }
    emit("player_text", data_to_send, to=lobby_id)


# Events only the host (or lobby mods) can send
@socketio.on("add_tag")
def add_tag(data):
    """Broadcasts the tag that was added.

    data is in the format:
        data = {
            "body": "tag"
        }

    Sent data is in the format:
        data_to_send = {
            "body": "tag"
        }
    """
    lobby_id = session["lobby_id"]
    if not is_lobby_host(current_user.get_id(), lobby_id): 
        return
    tag = data["body"]
    # TODO: Add tag to database
    data_to_send = {
        "body": tag
    }
    emit("add_tag", data_to_send, to=lobby_id)

@socketio.on("remove_tag")
def remove_tag(data):
    """Broadcasts the tag that was removed.

    data is in the format:
        data = {
            "body": "tag"
        }

    Sent data is in the format:
        data_to_send = {
            "body": "tag"
        }
    """
    lobby_id = session["lobby_id"]
    if not is_lobby_host(current_user.get_id(), lobby_id): 
        return
    tag = data["body"]
    # TODO: Remove tag from database
    data_to_send = {
        "body": tag
    }
    emit("remove_tag", data_to_send, to=lobby_id)

@socketio.on("change_lobby_name")
def change_lobby_name(data):
    """Broadcasts the new lobby name.

    data is in the format:
        data = {
            "body": "new lobby name"
        }

    Sent data is in the format:
        data_to_send = {
            "body": "new lobby name"
        }
    """
    lobby_id = session["lobby_id"]
    if not is_lobby_host(current_user.get_id(), lobby_id): 
        return
    new_lobby_name = data["body"]
    # TODO: Update lobby name in database
    data_to_send = {
        "body": new_lobby_name
    }
    emit("change_lobby_name", data_to_send, to=lobby_id)

@socketio.on("change_description")
def change_description(data):
    """Broadcasts the new description.

    data is in the format:
        data = {
            "body": "new description"
        }

    Sent data is in the format:
        data_to_send = {
            "body": "new description"
        }
    """
    lobby_id = session["lobby_id"]
    if not is_lobby_host(current_user.get_id(), lobby_id): 
        return
    new_description = data["body"]
    # TODO: Update lobby description in database
    data_to_send = {
        "body": new_description
    }
    emit("change_lobby_name", data_to_send, to=lobby_id)

@socketio.on("change_time_schedule")
def change_time_schedule(data):
    """Broadcasts the new time schedule.

    data is in the format:
        data = {
            "body": "new time schedule"
        }

    Sent data is in the format:
        data_to_send = {
            "body": "new time schedule"
        }
    """
    lobby_id = session["lobby_id"]
    if not is_lobby_host(current_user.get_id(), lobby_id): 
        return
    new_time_schedule = data["body"]
    # TODO: Update lobby time schedule in database
    data_to_send = {
        "body": new_time_schedule
    }
    emit("change_time_schedule", data_to_send, to=lobby_id)

def is_lobby_host(user_id, lobby_id):
    """Checks if user_id is the host of lobby_id."""
    # TODO
    return True