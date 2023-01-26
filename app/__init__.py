# Import the Flask Class from the flask module - will be main object
from flask import Flask
# Import SQLAlchemy and Migrate from their modules
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
# Import the Config class from the config module - will have all of the app's configurations
from config import Config

# Create an instance of the Flask Class called app
app = Flask(__name__)
# Configure the app using the Config class
app.config.from_object(Config)

# Allow CORS for all origins
CORS(app)

# Create an instance of SQLAlchemy to represent our database
db = SQLAlchemy(app)
# Create an instance of Migrate to represent our migration engine
migrate = Migrate(app, db)
# Create an instance of LoginManager to set up login functionality
login = LoginManager(app)
# Set the login view to redirect unauthorized users
login.login_view = 'login'
login.login_message = 'You must be logged in to perform this action'
login.login_message_category = 'danger'

# Import the api blueprint and register it with the Flask Application
from app.blueprints.api import api
app.register_blueprint(api)

# import all of the routes from the routes file into the current folder
from . import routes, models
