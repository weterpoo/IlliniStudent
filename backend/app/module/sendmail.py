import os


class InValidEmailError(Exception):
    pass


def send_mail(message, subject, *email):
    """Sends email using mail"""
    if not email:
        raise InValidEmailError('No email passed')
    if not message:
        raise InValidEmailError('No message passed')

    subject = "\"%s\nContent-Type: text/html\"" % (subject)
    for mail in email:
        cmd = "echo \'%s\'" % (message)
        cmd += " | "
        cmd += "mail -s "
        cmd += "%s " % (subject)
        cmd += "%s" % (mail)
        # Sadly due to os.system, we lose error checking....
        print "SUBJECT\n%r" % (subject)
        print "CMD\n%r" % (cmd)
        os.system(cmd)

def test_mail():
    cmd = 'echo \'<a href="www.google.com">google</a><br>This is how you link google\' | mail -s "TEST\nContent-Type: text/html" ikeda.shot@gmail.com'
    os.system(cmd)


