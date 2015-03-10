import MySQLdb as mdb


class ManageTable(object):

    def __init__(self, net_loc, user, password, db):
        """Initialize which user to login as"""
        self.con = mdb.connect(net_loc, user, password, db)

    def create(self, tbl_name, *args):
        """Initialize a table with certain elements"""
        with self.con:

            cur = self.con.cursor()
            command = "DROP TABLE IF EXISTS %s;" % (tbl_name)
            cur.execute(command)

            tbl_args = ""
            for key, value in args:
                tbl_args += " %s %s," % (key, value)

            tbl_args = tbl_args.rstrip(",")   # remove the last comma

            command = "CREATE TABLE %s(%s)" % (tbl_name, tbl_args)
            cur.execute(command)
        return tbl_name

    def describe(self, tbl):
        """mimics the describe function that mysql provides"""
        with self.con:
            cur = self.con.cursor()
            cur.execute("DESCRIBE %s" % (tbl))
            dataset = cur.fetchall()
            return dataset

    def insert(self, tbl, *val):
        """Insert a row of data into a table of choice"""
        with self.con:
            cur = self.con.cursor()
            values = ""
            for element in val:
                if element == 'NULL':
                    values += "NULL,"
                else:
                    values += "\'%s\'," % (element)
            values = values.rstrip(",")
            command = "INSERT INTO %s VALUES(%s)" % (
                tbl, values)
            cur.execute(command)

    def retrieve(self, tbl):
        """Obtains data from database as a Tuple"""
        with self.con:
            cur = self.con.cursor()

            cur.execute('SELECT * FROM %s' % (tbl))
            datatpl = cur.fetchall()

            return datatpl