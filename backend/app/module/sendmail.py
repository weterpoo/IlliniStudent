import os


class InValidEmailError(Exception):
    pass


def send_mail(message, subject, *email):
    """Sends email using mail"""
    if not email:
        raise InValidEmailError('No email passed')
    if not message:
        raise InValidEmailError('No message passed')

    for mail in email:
        cmd = "echo \'%s\'" % (message)
        cmd += " | mail -s "
        cmd += ' \"%s\nContent-Type: text/html\" ' % (subject)
        cmd += "%s" % (email)
        # Sadly due to os.system, we lose error checking....
        print "SUBJECT\n%r" % (subject)
        print "CMD\n%r" % (cmd)
        os.system(cmd)

def test_mail(subject, email):
    # How to do it in a single line:
    # cmd = 'echo \'<a href="www.google.com">google</a><br>This is how you link google\' | mail -s "TEST\nContent-Type: text/html" ikeda.shot@gmail.com'
    html_things = "<a href=\"www.google.com\">google</a><br>This is how you link google"
    
    cmd = "echo \'%s\'" % (html_things)
    cmd += " | mail -s "
    cmd += ' \"%s\nContent-Type: text/html\" ' % (subject)
    cmd += "%s" % (email)
    os.system(cmd)
