###################################################################################
# opendatabase.py
# Dependencies, MySQLdb
#
# This is the main function used to communicate with the database.
# Make sure you create an Object of ManageTable first, or the functions will
# not work as expected.
#
# You also must have a MySQL user authorized the access the specific database
# you are attempting to read, write, create, etc. to the tables.
#
# TODO
# - Must create a delete() function to delete an element in the tables
# - Must create a update() function to update the table, deleting old
# or expired elements in the table.
#
# This module is written to be flexible as possible, please keep it that way.
# If you do not understand how the module accesses/writes to the database, you
# may want to look into MYSQL and how tables are created
###################################################################################

import MySQLdb as mdb
import time
from datetime import datetime


class FormatError(Exception):
    pass


class ManageTable(object):

    def __init__(self, net_loc, user, password, db):
        """
        Initialize which user to login as.
        ManageTable(<Login Location>, <Username>, <Password>, <Database Name>)

        Example:
        db = ManageTable('localhost', 'testuser', 'thisisapassword', 'testdb')

        Note:
        Make sure you have created the user, with access to the database you
        are connecting to.
        """
        self.net = net_loc
        self.user = user
        self.passwd = password
        self.db = db
        self.con = mdb.connect(self.net, self.user,
                                self.passwd, self.db)

    def stale_fix(self):
        """
        Checks the mysql connection to see if everything is working as expacted.
        If there isn't, it initializes a new connection, so things do go
        smoothly.
        """
        try:
            cur = self.con.cursor()
            cur.execute("")
        except (AttributeError, MySQLdb.OperationalError):
            self.con = mdb.connect(self.net, self.user,
                                    self.passwd, self.db)
            cur.execute("")


    def create_new(self, tbl_name, *args):
        """
        Initializes a table with certain datatypes. Overwrites existing tables.

        create_new(<table name>, (<name of table element>, <variable type>), ...)
        *args must be passed as a tuple. You can pass more than 1 tuple to
        create more elements in the table

        create_new() returns the table name given. You can use this to guarentee
        that other functions are reading/writing to the same table.

        Example:
        db = ManageTable('localhost', 'testuser', 'thisisapassword', 'testdb')
        db.create_new('TestTable', ('Name', 'VARCHAR(20)'), ('Date', 'DATE'))
        """
        self.stale_fix()

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
        return None

    def create(self, tbl_name, *args):
        """
        Initialize a table with certain elements.
        The only difference between create_new() and create() is that
        create() will not delete the table if it exists.

        If the table already exists, it will not overwrite the table.

        create() also returns the name of the table. See create_new() for
        more information.

        Example:
        db = ManageTable('localhost', 'testuser', 'thisisapassword', 'testdb')
        db.create('TestTable', ('Name', 'VARCHAR(20)'), ('Date', 'DATE'))
        """
        self.stale_fix()

        # Quick Error checking:
        if not (type(args[0]) == tuple):
            FormatError('One or more element of args is not a tuple')

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
        return None

    def describe(self, tbl):
        """
        Mimics the describe function that mysql provides. Used mainly to
        debug what elements are in the table.

        Example:
        db = ManageTable('localhost', 'testuser', 'thisisapassword', 'testdb')
        tbl = db.create('TestTable', ('Name', 'VARCHAR(20)'), ('Date', 'DATE'))

        return db.describe(tbl)
        >>> Will return (('Name', 'VARCHAR(20)'), ('Date', 'DATE'))
        """
        self.stale_fix()

        with self.con:
            cur = self.con.cursor()
            cur.execute("DESCRIBE %s" % (tbl))
            dataset = cur.fetchall()
            return dataset
        return None

    def insert(self, tbl, *val):
        """
        Insert a row of data into a table of choice
        The values MUST follow the order and format of the data in the table.

        Use describe() if you are not sure what data formats are required
        (or use DESCRIBE <table name>; in MYSQL)

        Example:
        db = ManageTable('localhost', 'testuser', 'thisisapassword', 'testdb')
        tbl = db.create('TestTable', ('Name', 'VARCHAR(20)'), ('Date', 'DATE'))

        db.insert(tbl, 'Shotaro', '2015-03-11')

        >>> This will populate the first row of TestTable with
        "Shotaro | 2015-03-11"
        """
        self.stale_fix()

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
        """
        Obtains data from database as a Tuple.
        Function is deprecated! You can still use it though.

        Example:
        db = ManageTable('localhost', 'testuser', 'thisisapassword', 'testdb')
        tbl = db.create('TestTable', ('Name', 'VARCHAR(20)'), ('Date', 'DATE'))
        db.insert(tbl, 'Shotaro', '2015-03-11')

        return db.retrieve(tbl)
        >>> will return ('Shotaro', '2015-03-11')
        """
        return self.findall(tbl)

    def generate_api(self, tbl):
        """
        Generates a dictionary which can be converted to json
        Also will add when the data was retrieved.

        Example:
        db = ManageTable('localhost', 'testuser', 'thisisapassword', 'testdb')
        tbl = db.create('TestTable', ('Name', 'VARCHAR(20)'), ('Date', 'DATE'))
        db.insert(tbl, 'Shotaro', '2015-03-11')

        return db.generate_api(tbl)
        >>> Will return
                        {"TABLE":
                           ({"Name": "Shotaro", "Date": "2015-03-11"})

                         "TIME":
                            { "UPDATED": "2015-03-25T21:55:09.401689"}
                        }
        """
        self.stale_fix()
        with self.con:
            cur = self.con.cursor(mdb.cursors.DictCursor)
            cur.execute('SELECT * FROM %s' % (tbl))
            return_tupl = cur.fetchall()
            return_dict = {}
            return_dict.update({ tbl : return_tupl,
                                "TIME": { "UPDATED": datetime.now()}})

            return return_dict
        return None

    def find(self, tbl_name, id_name=None, condition=None):
        """
        Returns the first value based on conditions.
        id_name must be passed on as a tuple.

        condition must be passed on as a string of a MYSQL condition statement.

        Example:
        db = ManageTable('localhost', 'testuser', 'thisisapassword', 'testdb')
        tbl = db.create('TestTable', ('Name', 'VARCHAR(20)'), ('Date', 'DATE'))
        db.insert(tbl, 'Shotaro', '2015-03-11')

        return db.find(tbl, ('Name'), "Date = '2015-03-11'")
        >>> Returns ('Name', 'Shotaro')
        """
        self.stale_fix()

        # Error Checking
        if not ((type(id_name) == tuple) or (id_name == None)):
            FormatError('id_name is not a tuple')

        if not ((type(condition) == str) or (condition == None)):
            FormatError('condition is not a tuple')

        # Preprocessing
        cond = " WHERE "
        if condition == None:
            cond = ";"
        else:
            cond += "%s;" % (condition)

        return_id = ""
        if id_name == None:
            return_id = "*"
        else:
            for item in id_name:
                return_id += "%s, " % (item)
            return_id = return_id.rstrip(", ")
        command = "SELECT %s FROM %s%s" % (return_id, tbl_name,
                                           cond)
        with self.con:
            cur = self.con.cursor()
            cur.execute(command)
            return_tupl = cur.fetchall()
            #only return a tuple if there is something in it
            if len(return_tupl) == 0:
                return None
            else:
                return return_tupl[0]
        return None

    def findall(self, tbl_name, id_name=None, condition=None):
        """
        Returns all specific values based on conditions.
        id_name must be passed on as a tuple.

        condition must be passed on as a string of a MYSQL condition statement.

        Example:
        db = ManageTable('localhost', 'testuser', 'thisisapassword', 'testdb')
        tbl = db.create('TestTable', ('Name', 'VARCHAR(20)'), ('Date', 'DATE'))
        db.insert(tbl, 'Shotaro', '2015-03-11')

        return db.find(tbl, ('Name'), "Date = '2015-03-11'")
        >>> Returns ('Name', 'Shotaro')
        """
        self.stale_fix()
        # Error Checking
        if not ((type(id_name) == tuple) or (id_name == None)):
            FormatError('id_name is not a tuple')

        if not ((type(condition) == str) or (condition == None)):
            FormatError('condition is not a tuple')

        # Preprocessing
        cond = " WHERE "
        if condition == None:
            cond = ";"
        else:
            cond += "%s;" % (condition)

        return_id = ""
        if id_name == None:
            return_id = "*"
        else:
            for item in id_name:
                return_id += "%s, " % (item)
            return_id = return_id.rstrip(", ")
        command = "SELECT %s FROM %s%s" % (return_id, tbl_name,
                                           cond)
        with self.con:
            cur = self.con.cursor()
            cur.execute(command)
            return_tupl = cur.fetchall()
            #only return a tuple if there is something in it
            if len(return_tupl) == 0:
                return None
            else:
                return return_tupl[0]
        return None
    def set_time(self):
        """
        Sets the current time. Used internally to figure out
        the last time something was written to the table.
        """
        self.curr_date = time.strftime("%Y-%m-%d")
        self.curr_time = time.strftime("%I:%M:%S%p")

    def get_date(self):
        """
        Used to return the current date.
        """
        return self.curr_date

    def get_time(self):
        """
        Used to return the current time.
        """
        return self.curr_time

    def delete(self, tbl, coloum, content):
        """
        Delete the row which satisfies content in certain coloum.
        """
        self.stale_fix()
        with self.con:
            cur = self.con.cursor()
            query = "DELETE FROM %s WHERE (%s = %s)" % (tbl, coloum, content)
            cur.execute(query)
            self.set_time()
