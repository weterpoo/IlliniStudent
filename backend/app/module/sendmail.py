import os


class InValidEmailError(Exception):
    pass


def send_mail(message, subject, *email):
    if not email:
        raise InValidEmailError('No email passed')
    if not message:
        raise InValidEmailError('No message passed')

    for mail in email:
        cmd = "echo \"%s\"" % (message)
        cmd += " | "
        cmd += "mail -s "
        cmd += "\"$(echo -e \"%s\nContent-Type: text/html\")\" "
        cmd += "%s" % (mail)
        # Sadly due to os.system, we lose error checking....
        os.system(cmd)

