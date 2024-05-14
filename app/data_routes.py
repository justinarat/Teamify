"""Defines all data routes that the server responds to"""

from flask import request, make_response, jsonify
from app import app


@app.route("/get-lobby-cards", methods=["GET"])
def get_lobby_cards():
    """Endpoint for getting lobby cards for the lobby searching page

    This endpoint takes a GET request with the query string format:
        ?count=<count>&search_tags=<tag1>&search_tags=<tag2>...&
            ignore_tags=<tag1>&ignore_tags=<tag2>...

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

    try:
        count = int(count)
    except ValueError:
        return make_response("Parameter 'count' must be an integer", 400)

    if count == 0:
        return make_response("Parameter 'count' must be greater than 0", 400)

    lobby_cards = []

    for i in range(count):
        lobby_cards.append(
            {
                "lobby_id": f"{i}",
                "game_title": f"game{i}_title",
                "lobby_name": f"lobby{i}_name",
                "lobby_description": f"lobby{i}_desc",
                "host": f"host{i}",
                "players": [f"player_{i}", f"player_{i+1}"],
                "next_available_time": "timeblock format",
            }
        )

    # TODO:
    # search_tags = request.args.getlist("search_tags")
    # ignore_tags = request.args.getlist("ignore_tags")
    # Query the database for "count" number of lobby data and put them in
    # data_to_send["lobby_cards"], but can't do this until databases have been setup in flask

    return { "lobby_cards": lobby_cards }
