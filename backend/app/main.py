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

def edit_task(user, old_assign, assignnm, classnm, desc, due_d, due_t, tags):
    cond = "assign_name = \'%s\'" %(assignnm)
    task = access.find(user, ('assign_name', 'class_name',
                       'description', 'due_date',
                       'due_time', 'tags'), cond)
    if assignnm is None:
        assignnm = task[0][0]
    if classnm is None:
        classnm = task[0][1]
    if desc is None:
        desc = task[0][2]
    if due_d is None:
        due_d = task[0][3]
    if due_t is None:
        due_t = task[0][4]
    if tags is None:
        tags = task[0][5]

    access.delete(user, "assign_name", old_assign)
    access.insert(user, assignnm, classnm, desc,
                         due_d, due_t, tags)


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
