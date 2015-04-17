from flask import Flask
from flask.ext.cors import CORS
from flask.ext.mail import Mail

app = Flask(__name__)
cors = CORS(app)
mail = Mail(app)

app.config.from_object('app.config')

from app import views
