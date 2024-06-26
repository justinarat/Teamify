"""Initialise flask app and database"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "account_creation"
socketio = SocketIO(app, manage_session=False)

from app import routes, form_routes, model, socketevents, data_routes
from app.database.seed import seed_required, seed_all
import click


@app.cli.command("seed")
@click.argument("all_str", type=str, default="required", required=False)
def seed_command(all_str):
    """Seeds the database with just required, or all data"""
    print("Dropping all data...\n")
    db.drop_all()

    db.create_all()
    if all_str == "all":
        seed_all()
    else:
        seed_required()
