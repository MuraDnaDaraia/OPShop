from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'tutanxamoni'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\geoga\\PycharmProjects\\Finaluri\\instance\\database.db'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'