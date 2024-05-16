from app import create_app, db
from app.config import TestConfig
from flask_migrate import Migrate

app = create_app(TestConfig)
migrate = Migrate(db, app)
