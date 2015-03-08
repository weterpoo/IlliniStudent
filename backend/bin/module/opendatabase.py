import MySQLdb as mdb

class ManageTable(object):
    """Creates a test table, only to be used for demo purposes"""

    def __init__(self, net_loc, user, password, db):
        """Initialize which user to login as"""
        self.con = mdb.connect(net_loc, user, password, db)

    def create(self, tbl_name, **kwargs):
        """Initialize a table with certain elements"""
        with self.con:

            cur = self.con.cursor()
            command = "DROP TABLE IF EXISTS %s;" % (tbl_name)
            cur.execute(command)

            tbl_args = ""
            for key, value in kwargs.items():
                tbl_args += " %s %s," % (key, value)
            
            tbl_args = tbl_args.rstrip(",") # remove the last comma

            command = "CREATE TABLE %s(%s)" % (tbl_name, tbl_args)
            cur.execute(command)
        return tbl_name

    def insert(self, tbl, var, *val):
        """Insert data into a table of choice"""
        with self.con:
            cur = self.con.cursor()
            for elements in val:
                command = "INSERT INTO %s(%s) VALUES(%s)" % (tbl, var, elements)
                cur.execute(command)

    def retrieve(self, tbl):
        """Obtains data from database as a dictionary format"""
        with self.con:
            cur = self.con.cursor(mdb.cursors.DictCursor)

            cur.execute('SELECT * FROM %s' % (tbl))
            datadict = cur.fetchall()
            
            return datadict
            
