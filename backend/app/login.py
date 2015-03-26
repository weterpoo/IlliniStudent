##################################################################################
# login.py
# 
# Handles all the login and table creation based on user login.
##################################################################################

from modules.opendatabase import ManageTable as mt

def login(username, userpass):
    access = mt('localhost', 'checkuser', 'ch3ckEDl0CAL', 'studentdb')
    
