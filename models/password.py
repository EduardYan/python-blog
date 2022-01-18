"""
This module have the model
for the password encrypted
"""

class Password:
  """"
  Create a password
  with a value in bytes
  """

  def __init__(self, value:bytes):
    if type(value) not in [bytes]:
      raise TypeError('The value of the password must be bytes')

    self.value = value
    self.len = len(value.decode())