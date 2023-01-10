from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-duper-secret(not)'

# import all of the routes from the routes file into the current folder
from . import routes
