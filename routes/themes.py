"""
This file have the routes
for the blog in the server.
"""

from flask import Blueprint, render_template, flash, redirect, url_for
from utils.validations import validate_user

themes = Blueprint('themes', __name__)

# route for default
DEFAULT_ROUTE = 'themes.gnu_linux'


# routes for each theme
@themes.route('/<username>')
def home(username):
  """
  Manage the principal route of the server.
  """

  # validating if the user is in the datsbase
  if validate_user(username):
    # flash(f'Welcome {username} !!')
    return redirect(url_for(DEFAULT_ROUTE, username = username))

  else:
    # in case not is logged
    return render_template('accounts/create-account.html')


@themes.route('/gnu-linux/<username>')
def gnu_linux(username):
  """"
  Route for render the page
  of gnu/linux
  """

  if validate_user(username):
    return render_template('themes/gnu-linux.html', username = username)
  else:
    # in case not is logged
    return render_template('accounts/create-account.html')


@themes.route('/programming/<username>')
def programming(username):
  """
  Route for render the page
  of compilation
  """

  if validate_user(username):
    return render_template('themes/programming.html', username = username)

  else:
    return render_template('accounts/create-account.html')

@themes.route('/programs/<username>')
def programs(username):
  """
  Route for render the page for
  the program page
  """

  if validate_user(username):
    return render_template('themes/programs.html', username = username)
  else:
    return render_template('accounts/create-account.html')


@themes.route('/contacts/<username>')
def contacts(username):
  """"
  Render the page with the contacts
  """

  if validate_user(username):
    return render_template('contacts.html', username = username)

  else:
    return render_template('accounts/create-account.html')