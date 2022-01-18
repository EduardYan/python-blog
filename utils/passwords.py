"""
This module have some functions
for use for work with the passwords
"""

from bcrypt import hashpw, gensalt
from models.users import Users

def encrypt_password(value:bytes):
  """
  Return the password encrypted,
  raise TypeError, if the value not is bytes
  
  """

  salt = gensalt()
  # hashing
  password_hashed = hashpw(value, salt)

  return password_hashed
