# Import the Flask Class from the flask module - will be main object
from flask import Flask
# Import SQLAlchemy and Migrate from their modules
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# Import the Config class from the config module - will have all of the app's configurations
from config import Config

# Create an instance of the Flask Class called app
app = Flask(__name__)
# Configure the app using the Config class
app.config.from_object(Config)

# Create an instance of SQLAlchemy to represent our database
db = SQLAlchemy(app)
# Create an instance of Migrate to represent our migration engine
migrate = Migrate(app, db)
# Create an instance of LoginManager to set up login functionality
login = LoginManager(app)


# import all of the routes from the routes file into the current folder
from . import routes, models
