from module.sendmail import send_mail as sm
from passlib.apps import custom_app_context as pwd_context
from module.opendatabase import ManageTable as mt
import login
import random
import time


def send_confirm(userin, emailin, passin, netidin, majorin, gradin):
    access = mt('localhost', 'authorized', 'aCep0ted0dd', 'studentdb')

    cond = "username = \'%s\' or useremail = \'%s\' or usernetid = \'%s\'" % (userin,
                                                                              emailin,
                                                                              netidin)
    result = access.find("userinfo", ('username', 'useremail', 'usernetid'), cond)

    if not (len(result) == 0):
        # return something when it already exists
        return "Error -1: user exists. Please contact for help."

    salt = generate_salt(random.randint(7, 10))
    salt += userin + passin + netidin
    salt = pwd_context.encrypt(salt)
    passwd_final = pwd_context.encrypt(passin)
    store_temp(userin, emailin, passwd_final, netidin, majorin, gradin, salt)

    # Creating the email message
    subject = "Welcome to IlliniStudent!"
    body = "Hello %s,\n" % (userin)
    body += "Welcome to IlliniStudent! We are very happy to have you.\n"
    body += "Please click the link below to activate your account.\n"
    body += "We hope you enjoy this service!\n"
    body += "illinistudent.cu.cc:5000/jqconfirmlogin?id=%s" % (salt)

    sm(body, subject, emailin)


def generate_salt(num):
    salt = ''
    for i in range(0, num):
        salt += chr(random.randint(65, 122))
    return salt


def store_temp(userin, emailin, passin, netidin, majorin, gradin, salt):
    access = mt('localhost', 'authorized', 'aCep0ted0dd', 'studentdb')
    now = time.strftime("%Y-%m-%d")

    # Store information in the temp
    access.insert("temp", userin, emailin, passin, netidin,
                  majorin, gradin, salt, now)


def check_id(idin):
    """
    Checks for the id then creates the user.
    """
    access = mt('localhost', 'authorized', 'aCep0ted0dd', 'studentdb')
    cond = "confirmid = %s" % (idin)
    userinfo = access.findall("temp",
                   ("username", "useremail",
                    "userpass", "usernetid",
                    "usermajor", "usergrad"), cond)
    if len(userinfo) == 0:
        return "Error -1: No user found"

    user = login.create_login(userinfo[0], userinfo[1], userinfo[2],
                              userinfo[3], userinfo[4], userinfo[5])

    send_thank_you(userinfo[1])

    return user[1]


def send_thank_you(email):
    subject = "Welcome to IlliniStudent!"
    body = "You have succesfully registered for IlliniStudent!\n"
    body += "We will be continuously adding features, "
    body += "and we hope you look forward to them!\n"

    sm(subject, body, email)


def send_email_to(email):
    print "sending email now!"
    sm("Hello, this is Shotaro.", "Testing", email)
