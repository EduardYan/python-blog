""""
This file have the configuration
for the server,
execute the index.py for run 
the servver

"""

from flask import Flask
from routes.themes import themes
from routes.about import about_routes
from routes.auth import users
from routes.login import login_routes
from routes.account import account_routes
from flask_sqlalchemy import SQLAlchemy
from config import SQLITE_CONNECTION

# creating
app = Flask(__name__)

# settings
app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mysecrectkey'

# connecting
SQLAlchemy(app)


# using routes
app.register_blueprint(themes)
app.register_blueprint(about_routes)
app.register_blueprint(users)
app.register_blueprint(login_routes)
app.register_blueprint(account_routes)