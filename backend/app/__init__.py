from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
app.config.from_object('app.config')

cors = CORS(app)

from app import views
