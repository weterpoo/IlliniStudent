import MySQLdb as mdb
import time
from datetime import datetime


class ManageTable(object):

    def __init__(self, net_loc, user, password, db):
        """Initialize which user to login as"""
        self.con = mdb.connect(net_loc, user, password, db)

    def create_new(self, tbl_name, *args):
        """Initializes a table with certain elements.
        overwrites existing tables."""

        with self.con:
            cur = self.con.cursor()
            command = "DROP TABLE IF EXISTS %s" % (tbl_name)
            cur.execute(command)
            
            tbl_args = ""
            for key, value in args:
                tbl_args += " %s %s," % (key, value)
            tbl_args = tbl_args.rstrip(",")   # remove the last comma
            command = "CREATE TABLE IF NOT EXISTS %s(%s)" % (tbl_name, tbl_args)
            cur.execute(command)
        self.set_time()
        return tbl_name

    def create(self, tbl_name, *args):
        """Initialize a table with certain elements"""
        with self.con:
            cur = self.con.cursor()
            tbl_args = ""
            for key, value in args:
                tbl_args += " %s %s," % (key, value)

            tbl_args = tbl_args.rstrip(",")   # remove the last comma

            command = "CREATE TABLE IF NOT EXISTS %s(%s)" % (tbl_name, tbl_args)
            cur.execute(command)
        self.set_time()
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
        self.set_time()

    def retrieve(self, tbl):
        """Obtains data from database as a Tuple"""
        with self.con:
            cur = self.con.cursor()

            cur.execute('SELECT * FROM %s' % (tbl))
            datatpl = cur.fetchall()

            return datatpl

    def generate_api(self, tbl):
        """Generates a dictionary which can be converted to json
        file"""
        with self.con:
            cur = self.con.cursor(mdb.cursors.DictCursor)
            cur.execute('SELECT * FROM %s' % (tbl))
            return_tupl = cur.fetchall()
        return_dict = {}
        return_dict.update({"ASSIGNMENTS": return_tupl,
                            "TIME": { "UPDATED": datetime.now()}})
                                       
        return return_dict

    def set_time(self):
        self.curr_date = time.strftime("%Y-%m-%d")
        self.curr_time = time.strftime("%I:%M:%S%p")

    def get_date(self):
        return self.curr_date

    def get_time(self):
        return self.curr_time

# TODO: delete(), update()
# delete(): it will delete an element specified an element
# update(): it will check which assignments are completed, then deletes them
