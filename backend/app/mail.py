from module.sendmail import send_mail as sm
from passlib.apps import custom_app_context as pwd_context
from module.opendatabase import ManageTable as mt
import random
import time


def send_confirm(emailin, userin, passin, netidin, majorin, gradin):
    salt = generate_salt(random.randint(7, 10))
    salt += userin + passin + netidin
    salt = pwd_context.encrypt(salt)
    store_temp(emailin, userin, passin, netidin, majorin, gradin, salt)

    #Creating the email message
    subject = "Welcome to IlliniStudent!"
    body = "Hello %s,\n" % (userin)
    body += "Welcome to IlliniStudent! We are very happy to have you.\n"
    body += "Please click the link below to activate your account.\n"
    body += "We hope you enjoy this service!\n"
    body += "illinistudent.cu.cc:5000/jqactivate?id=%s" % (salt)

    sm(body, subject, emailin)



def generate_salt(num):
    salt = ''
    for i in range(0, num):
        salt += chr(random.randint(65, 122))
    return salt


def store_temp(emailin, userin, passin, netidin, majorin, gradin, salt):
    access = mt('localhost', 'authorized', 'aCep0ted0dd', 'studentdb')
    now = time.strftime("%Y-%m-%d")

    # Store information in the temp
    access.insert("temp", emailin, userin, passin, netidin,
                  majorin, gradin, salt, now)


def send_email_to(email):
    sm("Hello, this is Shotaro.", "Testing", email)
