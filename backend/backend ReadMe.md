# IlliniStudent Backend
#To do:
    1. Tabluate information the way it is represented in the jpg (it's on facebook chat!)

    2. Figure out a way to parse webpages to obtain information.

#Required modules:
    1. To be able to contribute you need to install*
       - virutalenv (optional, but recommended)
       - mysql-server
       - python-mysqldb (install in virtualenv)
       - nose (aka nosetests, not required to run the actual, only for test cases)
       - flask (install in vitualenv)

    2. Python 2.7.x

# Installing all of the packages
  <p>Before we start: this is assuming you have Linux distro. Specific steps may be different if you have Windows or Mac OS. (Though most of everything should work on Mac except for apt-get)

  1. Python 2.7.x is easy to install. Go to the python website

  2. Install pip
     <p>pip has great documentation to install it, make sure you add it to path.
     <p>To check if pip is installed correctly, type
     ```
     $ pip
     ```
     <p>It should spit out some documentation on how to use pip on the command line.

  3. Install virtualenv
     <p>Type:
     ```
     $ pip install virtualenv
     ```
     <p>That should fetch you the latest version of virtualenv

     <p>Test to see if virtualenv is working
     ```
     $ virtualenv
     ```
     <p>That should spit out documentation on how to use virtualenv on the command line
     <p>If it does not work, you may need to <em>add python's script folder to path</em>
     
  4. Installation using virtualenv (installing Python-MySQLdb, nose, flask)
    <p>Make sure that virtualenv is installed. (Done on previous step)
    <p>Now type
    ```
    $ virtualenv --distribute venv
    ```
    <p>The "venv" can be replaced with anything, it will become the name of the
    folder where all of the modules are stored.

    <p>If you do decide to call it something other than "venv" please add it to
    the .gitignore file, so it doesn't upload it to github

    <p>Now activate the venv, on Linux distros (and Mac OS) it is:
    ```
    $ source <name of folder>/bin/activate
    ```
    <p>if you called the folder "venv" (if you followed this example) you would
    replace <name of folder> with "venv" (obviously without the quotes)

    <p>If everything worked you should see something like:
    ```
    (venv)shotaro@shotaro-ThinkPad-T400 ~/IlliniStudent$
    ```
    <p>As long as you see the (venv) in the front, you have correctly activated
    the venv

    <p><b>This is called "Activating the virtual enviornment (abbreviated
    venv)"</b>.

    <p>After activating the venv, you can install other packages without
    messing up your regular python install.
    ```
    (venv)$ pip install nosetests
    ```

    ```
    (venv)$ pip install MySQL-python
    ```

    ```
    (venv)$ pip install flask
    ```

    <p>Those three commands will install nosetests (nose), Python-MySQLdb,
    and flask in that order.

    <p>Note that you don't really need virtualenv to actually install all
    of these. However, it is good practice to install modules that
    will only be used in one project (like Python-MySQLdb) in a
    Virtual Enviornment.

    <p>To deactivate the virtualenv, type:
    ```
    $ deactivate
    ```

    Make sure you activate the virtualenv if you want to work on it! (The program might not work without it)

  5. Installing MySQL-server
     <p>Installing MySQL-server is a little different depending on
     the platform.

     <p>For Windows and Mac OS, use the community installer.
     That will include MySQL-server. (That is the main one
     you want). You also probably want the python extension
     too.

     <p>For Linux or cygwin:
     ```
     $ sudo apt-get install mysql-server
     ```
     <p>(I think it should work for cygwin, provided you install
     the apt-get extension)

<p>Congradulations, you are now ready to follow the steps to running the backend!
    
# Running the backend on your local machine:
1. You have to have the requirements above fulfilled
2. Set up mysql as the following:

   <p>login as root
   ```
   $ mysql -u root -p
   ```
   
   <p>Create the studentdb database
   ```
   $ CREATE DATABASE studentdb;
   ```
   
   <p>Tell mysql to use the studentdb (need this command to create the table in the right place
   ```
   USE studentdb;
   ```
   
   <p>Create the userinfo table
   ```
   $ CREATE TABLE userinfo(username VARCHAR(20) NOT NULL, useremail VARCHAR(40) NOT NULL, userpass VARCHAR(30) NOT NULL, usernetid VARCHAR(25) NOT NULL, usermajor VARCHAR(25), usergrad DATE);
   ```
   
   <p>Create the checkuser@localhost user
   ```
   $ CREATE USER 'checkuser'@'localhost' IDENTIFIED BY 'ch3ckEDl0CAL';
   ```
   
   <p>Create the authorized@locahost user
   ```
   $ CREATE USER 'authorized'@'localhost' IDENTIFIED BY 'aCep0ted0dd';
   ```
   
   <p>Grant all permissions on everything under studentdb to authorized@localhost.
   <p>This will be required to have create user specific tables.
   ```
   $ GRANT ALL ON studentdb.* TO 'authorized'@'localhost';
   ```
   
   <p>Grant all permissions on the userinfo table to checkuser@localhost.
   <p>This is done for security reasons (though it might not matter so much in the end)
   ```
   $ GRANT ALL ON studentdb.userinfo TO 'checkuser'@'localhost';
   ```

3. Now activate the flask server.

   <p>Change your directory to the backend
   ```
   $ cd ~/path/to/IlliniStudent/backend/
   ```
   
   <p>Activate your virtualenv (or not) for me it's:
   ```
   $ source venv/bin/activate
   ```
   <p>If you installed all of the python modules without activating the virtual enviroment, ths is not needed
   <p>Note that the venv might be different between everyone, it depends on what you called it
   <p>PLEASE PLEASE DO NOT UPLOAD THE VIRTUALENV TO GITHUB! (it causes problems for you too!)

   <p>Run the flask application: 
   ```
   $ python run.py
   ```
   <p>The flask server will run on your ip address (which can be dangerous so don't keep it running too long!) or you can access it by going to your web browser and typing
   ```
   localhost:5000
   ```
   <p>By default flask servers run on port 5000. See your console for more details on what port it is running at.


# Final Words
  <p>You can see our glorious application at illinistudent.cu.cc which is the front end.
  <p>To peek into the back end you can go to illinistudent.cu.cc:5000

  <p>Thanks to Peter Woo, Tadas Aleksonis, and Cameron Patrick for being
  awesome CAs!

  <p>Also thanks to our fellow group members! You (might) be able to find their names in their respective readmes.

  <p>Backend is created by Shotaro Ikeda, Derek Zhang, Zono Mei, and Jason Situ
  
