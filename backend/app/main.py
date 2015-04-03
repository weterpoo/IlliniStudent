from app.module.opendatabase import ManageTable as mt

access = mt('localhost', 'authorized', 'aCep0ted0dd', 'studentdb')


# def initialize():
#     print "creating database IlliniTest..."
#     tbl = db.create_new('IlliniTest', ('assign_name', 'VARCHAR(30)'),
#                     ('class', 'VARCHAR(20)'), ('due_date', 'DATE'),
#                     ('due_time', 'TIME'))
#     db.insert(tbl, 'Homework 5', 'MATH 285', '2015-03-11', '8:00')
#     db.insert(tbl, 'MP4', 'CS125', '2015-03-09', '20:00')
#     db.insert(tbl, 'LAST 170 Midterm', 'LAST 170', '2015-03-11', '15:00')

# def main():
#     initialize()
#     output = db.retrieve('IlliniTest')
#     return output

##################################################################################
#
# Task handling
#
##################################################################################

def getapi_task(user_name):
    output = access.generate_api(user_name)
    return output

def table_task(user_name):
    output = access.findall(user_name)
    return output

def add_task(u_name, u_assign, u_class, u_desc, u_dued, u_duet,
             u_tags):
    access.insert(u_name, u_assign, u_class, u_desc, u_dued, u_duet,
                  u_tags)

##################################################################################
#
# Schedule handling
#
##################################################################################

def getapi_schedule(user_name):
    tbl_name = "%s_schedule" % (user_name)
    return access.generate_api(tbl_name)

def table_schedule(user_name):
    tbl_name = "%s_schedule" % (user_name)
    return access.findall(tbl_name)

##################################################################################
#
# Update time returners
#
##################################################################################

def get_date():
    return access.get_date()

def get_time():
    return access.get_time()

if __name__ == '__main__':
    print "no tests atm"
