import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  # TODO: change this to actual db file, haven't done it yet as I'm not sure
  #       how it'll affect the db file
  SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db") 
  SQLALCHEMY_TRACK_MODIFICATIONS = False
