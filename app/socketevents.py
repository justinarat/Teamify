from app import socketio
from flask import session
from flask_socketio import emit, join_room, leave_room
import sys

# TODO:
# - Update database for each event if necessary

# data fields:
# - sender_username (could put into cookie)
# - lobby_code: user for socketio room] (could put into cookie)
# - body: different for each event, could be: tag name, lobby name, description, 
#         time schedule, text message, kicked player name

# Events for players joining or leaving
# Shouldn't need to update the database here to add the new player as it should 
#   have been done when the player joins the server (in the lobby_view endpoint)
@socketio.on("player_join")
def player_join():
    """Broadcasts the new player's username to players.
    
    Sent data is in the format:
        data_to_send = {
            "sender_username": "sender_username", 
        }
    """
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    join_room(lobby_id)
    sender_username = "USERNAME" # TODO: Query database for sender username
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
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    # TODO: remove player from lobby in database
    session.pop("lobby_id")
    sender_username = "USERNAME" # TODO: Query database for sender username
    leave_room(lobby_id)
    data_to_send = {
        "sender_username": sender_username
    }
    emit("player_leave", data_to_send, to=lobby_id)

@socketio.on("player_kick")
def player_kick(data):
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
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
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    sender_username = "USERNAME" # TODO: Query database for sender username
    text_message = data["body"]
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
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    if not is_lobby_host(sender_user_id): return
    tag = data["body"]
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
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    if not is_lobby_host(sender_user_id): return
    tag = data["body"]
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
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    if not is_lobby_host(sender_user_id): return
    new_lobby_name = data["body"]
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
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    if not is_lobby_host(sender_user_id): return
    new_description = data["body"]
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
    sender_user_id, lobby_id = session["user_id"], session["lobby_id"]
    if not is_lobby_host(sender_user_id): return
    new_time_schedule = data["body"]
    data_to_send = {
        "body": new_time_schedule
    }
    emit("change_time_schedule", data_to_send, to=lobby_id)

def is_lobby_host(user_id, lobby_id):
    """Checks if user_id is the host of lobby_id."""
    # TODO
    return True
