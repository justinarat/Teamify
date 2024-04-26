from app import app
from flask import request, jsonify

# Expected url: /get-lobby-cards?count=<count>
@app.route("/get-lobby-cards", methods=["GET"])
def get_lobby_cards():
  count = request.args("count")
  data_to_send = {"lobby_cards": []}
  # TODO: query the database for "count" number of lobby data and put them in data_to_send["lobby_cards"]
  #       Can't do this yet as databases haven't been setup yet in flask
  # Data to get: game title, lobby name?, lobby description, host, player list,
  #              next available time
  return jsonify(data_to_send)
