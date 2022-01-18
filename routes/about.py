"""
This module have the routes
for about pages
"""

from flask import Blueprint, render_template
from utils.validations import validate_user

about_routes = Blueprint('about_routes', __name__)

@about_routes.route('/about/<username>')
def about(username):
  """
  Render the page for the principal
  about

  """

  if validate_user(username):
    return render_template('about.html', username = username)

  else:
    return render_template('accounts/create-account.html')