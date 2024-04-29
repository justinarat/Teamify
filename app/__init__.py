from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "secre" # temp
socketio = SocketIO(app, manage_session=False)

from app import routes, socketevents
