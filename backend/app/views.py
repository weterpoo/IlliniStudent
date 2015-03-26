from flask import render_template, flash, redirect, request, url_for
from app import app
from app import main
from forms import LoginForm
import login
import json

#important variables to be used
user=None
password=None
signed_in=None

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    form = LoginForm()
    if request.method == 'POST':
        # Pass the args on the url as user and password
        if request.args.get('usr'):
            user = request.args.get('usr')
        else:
            user = form.user_name.data
        if request.args.get('pass'):
            password = request.args.get('pass')
        else:
            password = form.user_pass.data

        # Flash a message to the users
        flash(("Login Requested for ID=%s") % (user))
        signed_in = login.login(user, password)
        if signed_in == -1:
            return ("User not found.")
        elif signed_in == 2:
            return "Multiple Users found! Email for help"
        elif signed_in == 1:
            return "Wrong Password"
        elif signed_in == 0:
            return "Thanks for logging in!"#redirect(url_for("success"))
        else:
            return "Unknown Error Occured"
    else:
        return render_template('index.html',
                               form=form)

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
    seconds_str += "%s" % (seconds)

    return ("%s:%s:%s" % (hours_str, minutes_str, seconds_str))
