#IlliniStudent

<br>
# How-to-backend

<em>A comprehensive guide on backending - by yours truely shotaro <3 ;)</em>
<h2> Not so Table of Contents</h2>
1. About - Basics like what jquery is. Skip if you know it.
2. Formatting For this README - The general syntax used for this README. <b>READ THIS</b>
3. How to - List of urls and stuff following the syntax claimed on no. 2

<h1>About</h1>
<em>Basics of JQuery, JSON, etc</em>
<p>JQuery is pretty easy. It's a way for someone to pass in arguments into a web browser through urls. That means you can have something like name = "Shotaro" kinda like in Java/C/whatever without complications.
<p>JSON is also pretty easy. Just think of it as a weird way to format things so that
content on websites and programs you write locally can retrieve data.
<p>MySQL is a database managing program. You can think of it as a lot of tables and
stuff that stores personal data like tasks, schedules, usernames, etc.

<p> Now you are ready to move on!

<h1>Formatting For this README</h1>
<em>Syntax, the guide to this guide</em>
<p>For this guide I'm going to assume that you already know which url to go to.
Hint: go to <a href="illinistudent.cu.cc:5000/">Backend</a>
<p> So jquery is done through passing arguments. This is what it looks like:
```
illinistudent.cu.cc:5000/jqlogin?name=MyUserName&pass=MySecretPass
```
This would pass in the variable "name" and "pass" into the flask server.
But how are you supposed to know which variables to use? You don't (and
aren't supposed to), which is why we have this guide!

<p> For the same example, the syntax for the guide will be the following:
<br>
```
/jqlogin
```
Takes in:<br>
      - \*user: the username of the user<br>
      - \*pass: the password of the user<br>
      - nothing: parameter to determine if the user likes to eat pies.<br>
<br>
The stars (\*) means that the columns are required. If you don't pass them in, there
will be an error passed back to you. How you handle it is up to you.
However, if there is no star (\*) and the user doesn't put anything in the column, don't
send any query! That means that if the user made the MyUserName account, the query
should look like the above.

<p> Ok, now it's time to move onto greater things!

<h1>How-to</h1>
<em>Do awesome stuff on the server</em>
<br>
```
/jqlogin
```
Takes in:<br>
      - \*user: the username of the user. password should not contain special symbols<br>
      - \*pass: the password of the user. right now it should be in plain text.<br>
Note: This is not the preferred method for logging in. See /jqaddtask for more details.<br>
<br>
<br>
```
/jqcreatelogin
```
Takes in:<br>
      - \*user: the username of the user. Should not contain special symbols.<br>
      - \*pass: the password of the user. Should be in plaintext<br>
      - \*email: the user's email. Make sure that it exists.<br>
      - \*netid: the user's netid.<br>
      - major: the user's current major.<br>
      - grad: the user's graduation date.<br>


<br>
<br>
```
/jqaddtask
```
Takes in:<br>
      - \*id: the user's authentication id. It is returned in json as auth_id<br>
      - \*assign: Assignment/activity name<br>
      - class: Class name. If there is none, it defaults to "Personal"<br>
      - desc: Description. If there is none, it defaults to a blank string.<br>
      - \*dued: Due Date. Please send it in YYYY-MM-DD format.<br>
      - duet: Due Time. Please send it in as HH:MM:SS.<br>
      - tags: Tags that the user may specify. Defaults to a blank string.<br>

<br>
<br>
```
/jqedittask
```
<em>This is not finished, Derek is working on it</em>

<br>
<br>
```
/jqtask
```
Takes in:<br>
      - \*id: The user's auth_id.<br>
Note: This is the preferred method for obtaining user information, or "logging in".<br>

<br>
```
/jqschedule
```
<em>This is not completely finished, there will bemore information soon.</em>

<br>
<br>
```
/jqsadboys
```
Takes in:<br>
      - \*id: The user's auth_id.<br>
Note: This deletes the user. We're sad they have to leave.<br>

<br>
<br>
```
/quickdel
```
Takes in:<br>
      - \*user: the username<br>
Note: This is the quick way to delete test cases. This will be removed in the final
release.<br>

<br>
```
/jqconfirmuser
```
Takes in:<br>
	  - \*id: the id that the user will send to you<br>
<br>
```
/jqresetpassword
```
	- email: the user's email<br>
	- netid: the user's netid<br>
Note: Please send at least one of the email or the netid. Both is fine, but would<br>
prefer to give the user a email or a netid option to recover the email<br>

<br>
```
/jqconfirmpassword
```
	- *id: the user's recovery_id that they will send you
