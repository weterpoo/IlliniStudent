import subprocess


class InValidEmailError(Exception):
    pass


def send_mail(message, subject, *email):
    """Sends email using mail"""
    if not email:
        raise InValidEmailError('No email passed')
    if not message:
        raise InValidEmailError('No message passed')

    for mail in email:
        ech = subprocess.Popen(['echo', message], stdout=subprocess.PIPE)
        output = subprocess.check_output(['mail', '-s', subject, mail],
                                         stdin=ech.stdout)
        ech.wait()
        print output
