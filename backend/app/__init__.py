from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config.from_object('app.config')

from app import views
