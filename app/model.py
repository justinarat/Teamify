from typing import List
from app import db

class Users(db.Model):
  UID = db.Column(db.Text(), primary_key=True, unique=True, nullable=False)
  Username = db.Column(db.Text(), nullable=False)
  Password = db.Column(db.Text(), nullable=False)
  Email = db.Column(db.Text(), unique=True, nullable=False)
