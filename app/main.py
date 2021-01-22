from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')

mail = Mail(app)
app.debug = 0
mail.init_app(app)

db = SQLAlchemy(app)

from .views import *
