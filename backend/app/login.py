##################################################################################
# login.py
# 
# Handles all the login and table creation based on user login.
##################################################################################

from module.opendatabase import ManageTable as mt
from passlib.apps import custom_app_context as pwd_context

salt = "not_so_random_salt"

def login(username, userpass):
    access = mt('localhost', 'checkuser', 'ch3ckEDl0CAL', 'studentdb')
    cond = "username = \'%s\'" % (username)
    pass_word = access.find("userinfo", ('userpass',), cond)

    print pass_word

    if len(pass_word) == 0:
        return -1
    else:
        checked_pass = pass_word[0]
        if len(pass_word) > 1:
            return 2
        elif not pass_equal(userpass, checked_pass):
            print "failed"
            return 1
        elif pass_equal(userpass, checked_pass):
            print "success!"
            return 0
        else:
            return -10

def login_jquery(other_authid):
    access = mt('localhost', 'checkuser', 'ch3ckEDl0CAL', 'studentdb')
    cond = "authid = \'%s\'" % (other_authid)

    u_info = access.find('userinfo', ('username', 'userpass'), cond)
    #return_dict = { "username": u_info[0]

    return u_info
    
def create_login(un, ue, up, uid, um, ug):
    access = mt('localhost', 'authorized', 'aCep0ted0dd', 'studentdb')
    # Check for optional fields
    if um == None:
        um = "NULL"
    if ug == None:
        ug = "NULL"

    # Hash password
    user_p = pass_hasher(up)

    # Hash ID
    user_id = generate_encrypt_id(un, up)

    cond = "username = \'%s\' or useremail = \'%s\' or usernetid = \'%s\'" % (un,
                                                                              ue,
                                                                              uid)
    result = access.find("userinfo", ('username', 'useremail', 'usernetid'), cond)
    if not (len(result) == 0):
        # return something when it already exists
        print "user exists"
        return False
    access.insert('userinfo', un, ue,
                  user_p, uid, um, ug, user_id)
    return login(un, up)
    
# Make a function to edit login info
# Password recovery function
# Find out to email

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

    jquery_result = login_jquery("$6$rounds=108441$5IQLSZTA4Q91OAJD$3uTUw53SFsocT5AyQ0YwVxGCkA0PECv9A3DfOcAN9GRiK.EQ6kKK1gC3OxKRZFFjlF4whCtfKGYz0djx97XSw1")
    
    print "Hello %s! Hope you have a good day!" % (jquery_result[0])

if __name__ == '__main__':
    main()
