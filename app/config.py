import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  # TODO: change this to actual db file, haven't done it yet as I'm not sure
  #       how it'll affect the db file
  SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "Database","MainDB.db") 
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.environ.get("CITS3403_FLASK_SECRET_KEY")
