import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("CITS3403_FLASK_SECRET_KEY")

class DeploymentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "Database","MainDB.db") 

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory"
    TESTING = True

