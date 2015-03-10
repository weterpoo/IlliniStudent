from module.opendatabase import ManageTable

db = ManageTable('localhost', 'testuser', 'test623', 'testdb')


def initialize():
    print "creating database IlliniTest..."
    tbl = db.create('IlliniTest', ('assign_name', 'VARCHAR(30)'),
                    ('class', 'VARCHAR(20)'), ('due_date', 'DATE'),
                    ('due_time', 'TIME'))
    print "writing testcases"
    db.insert(tbl, 'Homework 5', 'MATH 285', '2015-03-11', '8:00')
    db.insert(tbl, 'MP4', 'CS125', '2015-03-09', '20:00')
    db.insert(tbl, 'LAST 170 Midterm', 'LAST 170', '2015-03-11', '15:00')


def main():
    initialize()

if __name__ == '__main__':
    main()
