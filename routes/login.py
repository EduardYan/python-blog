"""
This module have the routes
for the login
"""

from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.password import Password
from models.users import Users
from utils.db import db
from bcrypt import checkpw

login_routes = Blueprint('login-routes', __name__)

@login_routes.route('/login', methods = ['GET', 'POST'])
def login():
  """
  This route is for the login
  validate if the method is GET
  or POST for save in the database
  or show the page.
  """

  # in case is get
  if request.method == 'GET':
    return render_template('login/login.html')

  else:
    # in case is post, getting data for save
    username = request.form['username']
    password = request.form['password']

    users = Users.query.all()
    
    names = []

    for user in users:
      names.append(user.name)

    # validating for not add if exits
    if username in names:

      password = Password(password.encode())

      # in case exists validating the password
      user = Users.query.filter_by(name = username).first()

      if checkpw(password.value, user.password.encode()):
        return redirect(url_for('themes.home' , username = username, password = user.password.encode()))

      else:
        flash('Password Incorrect')
        return redirect(url_for('login-routes.login'))

    else:
      return redirect(url_for('account-routes.create_account'))
