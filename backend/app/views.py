from flask import render_template, flash, redirect, request, url_for
from app import app
from app import main
from forms import LoginForm
import login
import json
import time

#important variables to be used
user=None
authid=None
signed_in=None

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    form = LoginForm()
    if request.method == 'POST':
        # Pass the args on the url as user and password
        global user
        user = form.user_name.data
        global password
        password = form.user_pass.data

        signed_in = login.login(user, password)
        if type(signed_in) == str:
            return render_template('fail.html',
                                   WARNING=signed_in,
                                   DATE=time.strftime("%Y-%m-%d"),
                                   TIME=time.strftime("%I:%M:%S%p")
                                   )
        else:
            global authid
            authid = signed_in[1]
            return redirect(url_for("taskview"))
    else:
        return render_template('index.html',
                               form=form,
                               DATE=time.strftime("%Y-%m-%d"),
                               TIME=time.strftime("%I:%M:%S%p")
                               )
        
# jquery related things go down here
@app.route('/jqtask')
# Handles jquery logins.
def jqtask():
    authid = request.args.get('id')
    userin = login.login_jquery(authid)

    global user
    user = userin.get("username")
    global authid
    authid = userin.get("authid")
    if user: 
        dictout = main.getapi(user)
        dictout.update({"authid": authid})
        return json.dumps(dictout, default=date_handler)
    else:
        return "Error: no id found"

@app.route('/jqschedule')
# Handles automated schedule fetching
def jqschedule():
    authid = request.args.get('id')
    userin = login.login_jquery(authid)

    global user
    user = userin.get("username")
    global authid
    authid = userin.get("authid")

    if user:
        dictout = main.getapi_schedule(user)
        dictout.update({"authid": authid})
        return json.dumps(dictout, default=date_handler)
    else:
        return "Error: no id found"

# Manual, user inputted pages
@app.route('/taskview')
# Handles manually logged in API browsers
def taskview():
    if user:
        output = main.table_info(user)
        return render_template("data.html",
                               output=output,
                               DATE=time.strftime("%Y-%m-%d"),
                               TIME=time.strftime("%I:%M:%S%p")
                               )
    else:
        flash("Log in before looking at tasks!")
        return redirect(url_for('index'))

@app.route('/taskapi')
# Get to the api manually
def taskapi():
    link = "/jqtask?id=%s" % (authid)
    return redirect(link)

@app.route('/scheduleview')
# get the schedule table
def scheduleview():
    if user:
        output = main.table_schedule(user)
        return render_template("sched.html",
                               output=output,
                               DATE=time.strftime("%Y-%m-%d"),
                               TIME=time.strftime("%I:%M:%S%p")
                               )
    else:
        flash("Login before getting your schedule!")
        return redirect(url_for('index'))

@app.route('/scheduleapi')
# Get to the schedule api manually
def scheduleapi():
    link = "/jqschedule?id=%s" % (authid)
    return redirect(link)

# json parsing functions
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
