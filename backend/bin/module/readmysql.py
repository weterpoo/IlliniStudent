import MySQLdb as mdb
import sys

def obtain_version():
    try:
        con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

        cur = con.cursor()
        cur.execute("SELECT VERSION()")

        ver = cur.fetchone()
        print "Database version : %s " % ver

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    finally:

        if con:
            con.close()

def fill_sample_data():
    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Writers")
        cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                    Name VARCHAR(25))")
        cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feutchwanger')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Truman Captole')")

def retrieve_data_all():
    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Writers")

        rows = cur.fetchall()
        for row in rows:
            print row

def retrieve_data_row():
    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Writers')
        for i in range(cur.rowcount):
            row = cur.fetchone()
            print row[0], row[1]
        
def dictionary_cursor():
    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

    with con:

        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute('SELECT * FROM Writers LIMIT 4')

        rows = cur.fetchall()

        for row in rows:
            # print row["Id"], row["Name"]
            # Just in case there is an error...
            print row.get('Id'), row.get('Name')

def column_headers():
    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Writers LIMIT 5")

        rows = cur.fetchall()

        desc = cur.description

        print "%s %3s" % (desc[0][0], desc[1][0])

        for row in rows:
            print "%2s %3s" % row

def print_newline():
    print "\n"
            
if __name__ == '__main__':
    print "Retriving Version....\n"
    obtain_version()
    print_newline()

    print "Filling MySQL Database with sample data...\n"
    fill_sample_data()

    print "Now retrieving ALL of the data at once... \n"
    retrieve_data_all()
    print_newline()

    print "Now retrieving the data ONE BY ONE...\n"
    retrieve_data_row()
    print_newline()

    print "Fetching Data using Dictionaries...\n"
    dictionary_cursor()
    print_newline()

    print "Fetching Column Headers...\n"
    column_headers()
    print_newline()
