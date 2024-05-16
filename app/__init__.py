from flask import Flask
from app.config import DeploymentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(DeploymentConfig)

    db.init_app(app)

    from app.blueprints import main
    app.register_blueprint(main)

    return app


from app import routes, model
