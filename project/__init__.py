from flask import Flask
from flask_login import LoginManager
from project.config.crypto import Crypto

app = Flask("project")
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from project.controllers import *
