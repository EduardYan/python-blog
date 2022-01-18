"""
This file have the routes
for the account
"""

from flask import Blueprint, render_template, request, flash, url_for, redirect
from models.users import Users
from models.password import Password
from utils.passwords import encrypt_password
from utils.db import db

# routes for the accounts
account_routes = Blueprint('account-routes', __name__)

@account_routes.route('/create-account', methods = ['GET', 'POST'])
def create_account():
  """
  Route for manage when the user
  create a new account
  """

  # validating the method
  if request.method == 'GET':
    return render_template('accounts/create-account.html')

  else: 
    # getting values
    username = request.form['username']
    password = request.form['password']

    password = Password(password.encode())

    if password.len < 6:
      flash('The password is less that 6. Try again.')

      return redirect(url_for('account-routes.create_account'))

    else:
      password_hashed = encrypt_password(password.value)

      user = Users(username, password_hashed.decode())
      db.session.add(user) # adding
      db.session.commit()


      return redirect(url_for('themes.home', username = user.name))


@account_routes.route('/myaccount/<username>')
def my_account(username):
  """
  Render the page for the
  account of the user.
  """

  # getting the user for pass to the page
  user = Users.query.filter_by(name = username).first()

  return render_template('accounts/myaccount.html', username = user.name, user = user)