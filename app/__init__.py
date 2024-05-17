from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import DeploymentConfig

db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    from app.blueprints import main
    app.register_blueprint(main)

    return app

app = create_app(DeploymentConfig) # Don't think this should be here but getting error without it

