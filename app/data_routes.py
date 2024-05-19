"""Defines all data routes that the server responds to"""

from flask import request, make_response, jsonify
from app import app
from app.model import Lobby, LobbyTimes, Games


@app.route("/get-lobby-cards", methods=["GET"])
def get_lobby_cards():
    """Endpoint for getting lobby cards for the lobby searching page

    This endpoint takes a GET request with the query string format:
        ?count=<count>
        &search_string=<search_string>
        &search_tags=<tag1>&search_tags=<tag2>...
        &ignore_tags=<tag1>&ignore_tags=<tag2>...

    The body of the response will also have json as:
    body = {
        "lobby_cards"=[
        {
            "lobby_id" : "1",
            "game_title": "game1_title",
            "lobby_name": "lobby1_name",
            "lobby_descrition": "lobby1_desc",
            "host": "host1",
            "players": ["player_1", "player_2", ...],
            "next_available_time": "timeblock format...",
        },
        {
            "lobby_id" : "2",
            "game_title": "game2_title",
            "lobby_name": "lobby2_name",
            "lobby_descrition": "lobby2_desc",
            "host": "host2",
            "players": ["player_a", "player_b", ...],
            "next_available_time": "timeblock format...",
        },
        ...
        ]
    }
    """

    if "count" not in request.args:
        return make_response("Parameter 'count' is missing", 400)

    count = request.args.get("count")

    if count is None:
        return make_response("Parameter 'count' is missing", 400)

    try:
        count = int(count)
    except ValueError:
        return make_response("Parameter 'count' must be an integer", 400)

    if count < 0:
        return make_response(
            "Parameter 'count' must be greater than or equal to 0", 400
        )

    if "search_string" not in request.args:
        return make_response("Parameter 'search_string' is missing", 400)

    search_string = request.args.get("search_string")
    search_tags = request.args.getlist("search_tags")

    lobbies = search_db(count, search_string, search_tags)

    lobby_cards = []
    for lobby in lobbies:
        player_usernames = [player.Username for player in lobby.players]
        lobby_card = {
            "lobby_id": lobby.LobbyID,
            "game_title": lobby.game.Name,
            "lobby_name": lobby.Name,
            "lobby_description": lobby.Desc,
            "host": lobby.get_host().Username,
            "players": player_usernames,
            "next_available_time": get_next_available_time(lobby),
        }
        lobby_cards.append(lobby_card)

    return jsonify({"lobby_cards": lobby_cards})


def search_db(count, search_string, search_tags):
    """Returns 'count' lobby IDs based on search params"""
    # Filter by tags
    lobby_query = Lobby.query
    for tag in search_tags:
        lobby_query = lobby_query.filter(Lobby.tags.has(Name=tag))

    # Check if search_string is in the lobby game name
    default_search = ""
    if search_string != default_search:
        lobby_query = lobby_query.join(Games).filter(Games.Name.contains(search_string))

    return lobby_query.limit(count).all()


def get_next_available_time(lobby):
    """Returns the next available time for a lobby"""
    lobby_time_query = LobbyTimes.query.filter_by(LobbyID=lobby.LobbyID)
    lobby_time_list = lobby_time_query.all()

    next_time_str = "No available times"
    if len(lobby_time_list) > 0:
        next_time = lobby_time_list[0]
        day = LobbyTimes.get_day_string(next_time)
        next_time_str = f"{day}: {next_time.TimeBlockStart} - {next_time.TimeBlockEnd}"

    return next_time_str
