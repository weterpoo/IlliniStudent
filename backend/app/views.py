from flask import render_template, flash, redirect, request, url_for, Response
from app import app
from app import main
from forms import LoginForm
import mail
import login
import json
import time
###############################################################################
# important variables to be used
###############################################################################

global user
global authid
global signed_in
global password

user = None
authid = None
signed_in = None
password = None


###############################################################################
# Flask Application Routes
###############################################################################
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


@app.route('/testmail')
def testmail():
    email = str(request.args.get('email'))
    mail.send_email_to(email)
    return "%r" % email
###############################################################################
# jquery related things go down here
###############################################################################

##############################
# "Logging in"
# 1. Used when user logins in a device without knowing their auth_id
# 2. Used when user creates an account
##############################

@app.route('/jqlogin')
def jqlogin():
    global user
    user = request.args.get('user')
    global password
    password = request.args.get('pass')

    result = login.login(user, password)
    print result
    if type(result) == int:
        return result
    else:
        global authid
        authid = result[1]

        return return_json_task()

@app.route('/jqcreatelogin')
def jqcreatelogin():
    userin = request.args.get('user')
    emailin = request.args.get('email')
    passin = request.args.get('pass')
    netidin = request.args.get('netid')
    majorin = request.args.get('major')
    gradin = request.args.get('grad')

    # Check if arguments are supplied
    if not userin:
        return "missing user parameter"
    elif not emailin:
        return "missing email parameter"
    elif not passin:
        return "missing pass parameter"
    elif not netidin:
        return "missing netid parameter"
    elif not majorin:
        majorin = "NULL"

    if not gradin:
        gradin = "0000-00-00"

    if (not (len(gradin) == 10) or
        not (gradin.rfind('-') == 7) or
        not (gradin.find('-') == 4)):
        return "grad is not in the right format."

    mail.send_confirm(userin, emailin, passin,
                       netidin, majorin, gradin)
    return "Registered Successfully!"

@app.route('/jqauthidlogin')
def jqauthidlogin():
    """Confirms the user using jquery"""
    input_id = request.args.get('id')
    global authid
    authid = login.login_jquery(input_id)

    return return_json_task()

@app.route('/confirmfromemail')
def confirmfromemail():
    userid = request.args.get('id')

    if not userid:
        return "login_id required"

    global authid
    authid = mail.check_id(userid)

    return "success"

@app.route('/jqresetpassword')
def jqresetpassword():
    email = request.args.get('email')
    netid = request.args.get('netid')

    global authid
    authid = login.recover_login(email, netid)
    return return_json_task()

@app.route('/jqchangepassword')
def jqchangepassword():
    userin = request.args.get('id')
    new_pass = request.args.get('new_pass')
    old_pass = request.args.get('old_pass')

    return login.change_password(old_pass, new_pass, userin)


@app.route('/jqconfirmpassword')
def jqconfirmpassword():
    recover_id = request.args.get('id')
    login.reset_password(recover_id)


@app.route('/jqaddtask')
def jqaddtask():
    authid = request.args.get('id')
    userin = login.login_jquery(authid)

    global user
    user = userin.get("username")
    global authid
    authid = userin.get("authid")

    if not user:
        return "not a valid id"

    # Get the parameters required
    u_assign = request.args.get('assign')
    u_class = request.args.get('class')
    u_desc = request.args.get('desc')
    u_dued = request.args.get('dued')
    u_duet = request.args.get('duet')
    u_tags = request.args.get('tags')

    # Check for Errors
    if not u_assign:
        return "assign is required"
    if not u_class:
        u_class = "Personal"
    if not u_desc:
        u_desc = ""
    if not u_dued:
        return "dued is required"
    elif (not (len(u_dued) == 10) or
          not (u_dued.rfind('-') == 7) or
          not (u_dued.find('-') == 4)):
        return "dued is not valid (needs YYYY-MM-DD)"
    if not u_duet:
        u_duet = "00:00:00"
    elif (not (len(u_duet) == 8) or
          not (u_duet.rfind(':') == 5) or
          not (u_duet.find(':') == 2)):
        return "duet is not valid (needs HH:MM:SS)"
    if not u_tags:
        u_tags = ""
    # Front end must make sure that the characters do not overflow
    main.add_task(user, u_assign, u_class, u_desc,
                  u_dued, u_duet, u_tags)

    return return_json_task()


@app.route('/jqedittask')
def jqedittask():
    userid = request.args.get('id')
    userin = login.login_jquery(userid)

    quick_user = userin.get("username")
    global authid
    authid = userin.get("authid")

    if authid is None:
        return "bad authid"

    old_assign = request.args.get("old_assign")
    assignnm = request.args.get("new_assign")
    classnm = request.args.get("class")
    desc = request.args.get("desc")
    due_d = request.args.get("dued")
    due_t = request.args.get("duet")
    tags = request.args.get("tags")

    main.edit_task(quick_user, old_assign, assignnm,
                   classnm, desc, due_d, due_t, tags)

@app.route('/jqdeletetask')
def jqdeletetask():
    userid = request.args.get('id')
    deletetask = request.args.get('name')
    userin = login.login_jquery(userid)

    if userin is None:
        return "bad id"
    if deletetask is None:
        return "no task name"

    main.delete_task(userin.get("username"), deletetask)
    return return_json_task()


##############################
# jquery to obtain user data
##############################
@app.route('/jqtask')
# Handles jquery logins.
def jqtask():
    global authid
    authid = request.args.get('id')

    return return_json_task()

@app.route('/jqschedule')
# Handles automated schedule fetching
def jqschedule():
    global authid
    authid = request.args.get('id')

    return return_json_schedule()

##################################################################################
# DANGER ZONE!
##################################################################################
@app.route('/jqsadboys')
# Deletes the user. Good bye :(
def jqsadboys():
    authid = request.args.get('id')
    userin = login.login_jquery(authid)
    return login.delete_user(userin.get("username"))

@app.route('/quickdel')
def quickdel():
    quick_user = request.args.get('user')
    return login.delete_user(quick_user)
    

##################################################################################
# Manual, user inputted pages
##################################################################################

####################
# Task related
####################
@app.route('/taskview')
# Handles manually logged in API browsers
def taskview():
    if user:
        output = main.table_task(user)
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

@app.route('/edittask')
# editing a task
def edittask():
    userid = request.args.get('id')
    userin = login.login_jquery(userid)

    quick_user = userin.get("username")
    global authid
    authid = userin.get("authid")

    if authid is None:
        return "bad authid"

    old_assign = request.args.get("old_assign")
    assignnm = request.args.get("new_assign")
    classnm = request.args.get("class")
    desc = request.args.get("desc")
    due_d = request.args.get("dued")
    due_t = request.args.get("duet")
    tags = request.args.get("tags")

    main.edit_task(quick_user, old_assign, assignnm,
                   classnm, desc, due_d, due_t, tags)


####################
# Schedule Related
####################
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

##################################################################################
# json parsing functions
##################################################################################

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


def return_json_task():
    userin = login.login_jquery(authid)

    global user
    user = userin.get("username")
    global authid
    authid = userin.get("authid")

    if user:
        dictout = main.getapi_task(user)
        dictout.update({"authid": authid})
        data = json.dumps(dictout, default=date_handler)
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp
    else:
        return "Error: no id found"

def return_json_schedule():
    userin = login.login_jquery(authid)

    global user
    user = userin.get("username")
    global authid
    authid = userin.get("authid")

    if user:
        dictout = main.getapi_schedule(user)
        dictout.update({"authid": authid})
        data = json.dumps(dictout, default=date_handler)
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp
    else:
        return "Error: no id found"
