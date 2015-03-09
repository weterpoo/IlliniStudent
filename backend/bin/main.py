from module.opendatabase import *


def testcase():
    db = ManageTable('localhost', 'testuser', 'test623', 'testdb')
    tbl = db.create('sample', ('name', 'VARCHAR(20)'),
                    ('date', 'DATE'), ('test', 'VARCHAR(50)'))

    for f, t, n, k, d, e in db.describe(tbl):
        print "Field: %s Takes in %s" % (f, t)

    db.insert(tbl, "Shotaro Ikeda", "1995-12-02", "my name")
    db.insert(tbl, "Professor", "0000-00-00", "mystery")
    db.insert(tbl, "Some random guy", "2015-02-23", "NULL")
    # db.insert(tbl, "A")

    getdb = db.retrieve(tbl)

    return getdb

if __name__ == '__main__':
    testing = testcase()
    print testing
    for n, d, t in testing:
        print "%25s    %10s     %10s" % (n, d, t)
        
