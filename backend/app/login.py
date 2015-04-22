passw = 'lel'
##################################################################################
# login.py
# 
# Handles all the login and table creation based on user login.
##################################################################################

from module.opendatabase import ManageTable as mt
from passlib.apps import custom_app_context as pwd_context
from module.sendmail import send_mail as sm

salt = "not_so_random_salt"

def login(username, userpass):
    access = mt('localhost', 'checkuser', 'ch3ckEDl0CAL', 'studentdb')
    cond = "username = \'%s\'" % (username)
    user_inf = access.find("userinfo", ('userpass', 'authid'), cond)

    if user_inf == None:
        return "Wrong Username"
    else:
        checked_pass = user_inf[0]
        if not pass_equal(userpass, checked_pass):
            return "Wrong Password"
        elif pass_equal(userpass, checked_pass):
            return user_inf
        else:
            return "Error -10: Unknown error. Please email for support."

def login_jquery(other_authid):
    access = mt('localhost', 'checkuser', 'ch3ckEDl0CAL', 'studentdb')
    cond = "authid = \'%s\'" % (other_authid)

    u_info = access.find('userinfo', ('username', 'authid'), cond)
    # return a blank dictionary if nothing was found
    if u_info == None:
        return {}
    else:
        return_dict = {"username": u_info[0], "authid": u_info[1]}

    return return_dict


def create_login(un, ue, up, uid, um, ug):

    access = mt('localhost', 'authorized', 'aCep0ted0dd', 'studentdb')
    authid = generate_encrypt_id(un, up)
    access.insert('userinfo', un, ue,
                  up, uid, um, ug, authid)
    # When the user creates an account, there should be two databases created
    # for the user
    # <username>_schedule
    # <username>

    table1 = "%s" % (un)
    table2 = "%s_schedule" % (un)
    access.create_new(table1, ('assign_name', 'VARCHAR(50) NOT NULL'),
                      ('class_name', 'VARCHAR(30)'),
                      ('description', 'VARCHAR(256)'),
                      ('due_date', 'DATE'), ('due_time', 'TIME'),
                      ('tags', 'VARCHAR(256)')
                      )
    access.create_new(table2, ('class', 'VARCHAR(128) NOT NULL'),
                      ('monday_start', 'TIME'),
                      ('monday_end', 'TIME'),
                      ('tuesday_start', 'TIME'),
                      ('tuesday_end', 'TIME'),
                      ('wednesday_start', 'TIME'),
                      ('wednesday_end', 'TIME'),
                      ('thursday_start', 'TIME'),
                      ('thursday_end', 'TIME'),
                      ('friday_start', 'TIME'),
                      ('friday_end', 'TIME'),
                      ('saturday_start', 'TIME'),
                      ('saturday_end', 'TIME'),
                      ('sunday_start', 'TIME'),
                      ('sunday_end', 'TIME'),
                      ('class_start', 'DATE'),
                      ('class_end', 'DATE')
                      )
    return login(un, up)


# Make a function to edit login info
# Password recovery function
# Find out to email
def recover_login(email, netid):
    """
    Helps password recovery. Sends an email with an autogenerated password
    """
    if not email and not netid:
        return "No email or netid."

    access = mt('localhost', 'authorized', 'aCep0ted0dd', 'studentdb')

    cond = ""
    if email:
        cond = "useremail = \'%s\'" % (email)
    elif netid:
        cond = "usernetid = \'%s\'" % (netid)
        
    result = access.find("userinfo",
                         ('username', 'useremail', 'recover_id'),
                         cond)
    name = result[0][0]
    email = result[0][1]
    recover_id = result[0][2]
    recover_message(name, email, recover_id)


def recover_message(name, email, link):
    subject = "IlliniStudent Recovery for %s" % (name)
    message = "Hello %s,\n" % (name)
    message += "We have gotten a request to reset your password.\n"
    message += "<b>If this was not you, please ignore this message.</b>\n"
    message += "Otherwise, click the link below to reset your password."
    message += " A new password will be emailed to you shortly.\n"
    message += "\n\n<a href=\"%s\"" % (link)
    message += ">RECOVER PASSWORD</a>."

    sm(message, subject, email)


# Encryption Handlers
def generate_encrypt_id(user_name, password):
    # Generates a unique id to jquery with
    encrypt_str = (salt + user_name + password)
    return pwd_context.encrypt(encrypt_str)

# Password Handlers
def pass_hasher(password):
    return pwd_context.encrypt(password)

def pass_equal(password, hashed_password):
    return pwd_context.verify(password, hashed_password)

def delete_user(name=None):
    access = mt('localhost', 'authorized', 'aCep0ted0dd', 'studentdb')
    if name:
        schedule_table = "%s_schedule" % (name)

        access.delete('userinfo', 'username', name)
        access.delete_table(name)
        access.delete_table(schedule_table)
        return "Success"

    return "No name of user specified."



# Test functions
def main():
    print "Trying User 1"
    login('SomethingRandom', 'abc123')
    print "Trying user 2"
    login('IlliniTester', 'illinistudent-server')

    create_login('IlliniTester', 'ikeda.shot@gmail.com',
                 'illinistudent-server', 'ikeda2', 'Computer Science',
                 '2015-05-00')
    create_login('SomethingRandom', 'random.rambo@gmail.com',
                 'abc123', 'rand123','GENERAL', '2099-12-00')

    jquery_result = login_jquery("$6$rounds=93721$q/WllrDVBZCHqQgU$5xnOxgqlvMJP4ZUhEbHNhiQ/YNYnvY636XdI/w1qrDegx/vwjeH9CJBPpEaKPpWtDya7BfEKSF/Msh328luP30")
    
    print "Hello %s! Hope you have a good day!" % (jquery_result.get("username"))

if __name__ == '__main__':
    main()
