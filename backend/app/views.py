import flask
from flask import JSONEncoder
from app import app
from app import main
import json

@app.route('/')
@app.route('/index')
def index():
    testout = main.main()
    curr_date = main.get_date()
    curr_time = main.get_time()
    return flask.render_template('index.html',
                           output=testout,
                           DATE = curr_date,
                           TIME = curr_time
                           )

@app.route('/webapi')
def webapi():
    dictout = json.dumps(main.getapi(), default=date_handler)
    curr_date = json.dumps(main.get_date(), default=date_handler)
    curr_time = json.dumps(main.get_time(), default=date_handler)
    return flask.jsonify(assignments=dictout,
                         UPDATE_DATE=curr_date,
                         UPDATE_TIME=curr_time
                         )
    
def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj
