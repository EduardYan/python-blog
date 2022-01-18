"""
Some functions for
the validations of the user

"""

from models.users import Users

def validate_user(username:str) -> bool:
  """
  Return True if the username
  passed for parameter is in the
  list of names of the database
  """

  users = Users.query.all()

  names = []

  for user in users:
    names.append(user.name)


  # validating if the user is in the datsbase
  return True if username in names else False