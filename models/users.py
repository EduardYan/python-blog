"""
This file have the model
for the user, in the database.
"""

from utils.db import db

class Users(db.Model):
  """
  Model for the users
  """

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(50))
  password = db.Column(db.String(200))

  def __init__(self, name:str, password:str) -> None:
    # values
    self.name = name
    self.password = password
