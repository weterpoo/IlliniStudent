#
# config.py contains configurations for the
# form submissions. (aka secret_key)
#

WTF_CSRF_ENABLED = True
SECRET_KEY = "somethingsomethingunrelated"

###############################################################################
# Mail Configuration
###############################################################################

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = 'do-not-reply'
MAIL_PASSWORD = 'replybot'

ADMINS = ['do-not-reply@mail.illinistudent.cu.cc']
