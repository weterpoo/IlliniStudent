from flask import render_template
from app import app
from app import main

@app.route('/')
@app.route('/index')
def index():
    testout = main.main()
    return render_template('index.html',
                           output=testout)
