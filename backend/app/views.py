import flask
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
    dictout = main.getapi()
    return json.dumps(dictout, default=date_handler)
    
def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    elif hasattr(obj, 'seconds'):
        return time_to_string(obj.seconds)
    else:
        raise TypeError("Unserializable object {} of type {}".format(obj, type(obj)))

def time_to_string(s):
    # Calculate hours, minutes, seconds, given the amount of seconds
    hours = s // 3600
    s -= (hours * 3600)
    minutes = s // 60
    seconds = s - (minutes * 60)
    # Make the hours, minutes look prettier, so they display
    # 08:02:10 instead of 8:2:10
    hours_str = ""
    minutes_str = ""
    seconds_str = ""
    if (hours < 10):
        hours_str = "0"
    if (minutes < 10):
        minutes_str = "0"
    if (seconds < 10):
        seconds_str = "0"
    hours_str += "%s" % (hours)
    minutes_str += "%s" % (minutes)
    seconds_str += "%s" % (minutes)

    return ("%s:%s:%s" % (hours_str, minutes_str, seconds_str))
