from flask import render_template
from app import app
from app import maintest

@app.route('/')
@app.route('/index')
def index():
    
    return "Hello, World!"
