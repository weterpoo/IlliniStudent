from module.opendatabase import *

if __name__ == '__main__':
    db = ManageTable('localhost', 'testuser', 'test623', 'testdb')
    tbl = db.create('sample', name='VARCHAR(20)', date='DATE', test='VARCHAR(50)')
