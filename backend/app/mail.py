from module.sendmail import send_mail as sm
from passlib.apps import custom_app_context as pwd_context
from module.opendatabase import ManageTable as mt
import random
import time


def send_confirm(emailin, userin, passin, netidin, majorin, gradin):
    salt = generate_salt(random.randint(7, 10))
    salt += namein + passin + netidin
    pwd_context.encrypt(salt)
    store_temp(salt)


def generate_salt(num):
    salt = ''
    for i in range(0, num):
        salt += chr(random.randint(65, 122))
    return salt


def store_temp(emailin, userin, passin, netidin, majorin, gradin, salt):
    access = mt('localhost', 'authorized', 'aCep0ted0dd', 'studentdb')


def send_email_to(email):
    pass
