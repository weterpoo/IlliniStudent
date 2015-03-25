# IlliniStudent Backend
#To do:
    1. Implement mysql to python (find a way to read/write to a mysql database)
    2. Implement flask to be able to spit out an api.
    3. Figure out a way to parse webpages to obtain information.
#Required modules:
    1. To be able to contribute you need to install*
       - virutalenv
       - mysql-server
       - python-mysqldb
       - nose (aka nosetests)
       - flask
       * Note: You might only need to install virtualenv, mysql-server. Try to activate the venv in the backend directory, then install packages. 
    2. Python 2.7.x

#To start developing:
    1. make sure you work within the Virtual enviorment.
       - for linux: $ cd backend
       - $ source venv/bin/activate

       - to deactivate the venv: $ deactivate



# Running the backend on your local machine:
1. You have to have the requirements above fulfilled
2. Set up mysql as the following:

   login as root
   ```
   $ mysql -u root -p
   ```
   
   Create the studentdb database
   ```
   $ CREATE DATABASE studentdb;
   ```
   
   Tell mysql to use the studentdb (need this command to create the table in the right place
   ```
   USE studentdb;
   ```
   
   Create the userinfo table
   ```
   $ CREATE TABLE userinfo(username VARCHAR(20) NOT NULL, useremail VARCHAR(40) NOT NULL, userpass VARCHAR(30) NOT NULL, usernetid VARCHAR(25) NOT NULL, usermajor VARCHAR(25), usergrad DATE);
   ```
   
   Create the checkuser@localhost user
   ```
   $ CREATE USER 'checkuser'@'localhost' IDENTIFIED BY 'ch3ckEDl0CAL';
   ```
   
   Create the authorized@locahost user
   ```
   $ CREATE USER 'authorized'@'localhost' IDENTIFIED BY 'aCep0ted0dd';
   ```
   
   Grant all permissions on everything under studentdb to authorized@localhost
   This will be required to have create user specific tables.
   ```
   $ GRANT ALL ON studentdb.* TO 'authorized'@'localhost';
   ```
   
   Grant all permissions on the userinfo table to checkuser@localhost.
   This is done for security reasons (though it might not matter so much in the end)
   ```
   $ GRANT ALL ON studentdb.userinfo TO 'checkuser'@'localhost';
   ```

3. Now activate the flask server.

   Change your directory to the backend
   ```
   $ cd ~/path/to/IlliniStudent/backend/
   ```
   
   Activate your virtualenv (or not) for me it's:
   ```
   $ source venv/bin/activate
   ```
   if you installed all of the python modules without activating the virtual enviroment, ths is not needed
   Note that the venv might be different between everyone, it depends on what you called it
   PLEASE PLEASE DO NOT UPLOAD THE VIRTUALENV TO GITHUB! (it causes problems for you too!)

   Run the flask application: 
   ```
   $ python run.py
   ```
   The flask server will run on your ip address (which can be dangerous so don't keep it running too long!) or you can access it by going to your web browser and typing
   ```
   localhost:5000
   ```
   By default flask servers run on port 5000. See your console for more details on what port it is running at.

