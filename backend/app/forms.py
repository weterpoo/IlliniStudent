from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
    user_name = StringField('user_name', validators=[DataRequired()])
    user_pass = PasswordField('user_pass', validators=[DataRequired()])

class NewLoginForm(Form):
    new_user_name = StringField('new_user_name',
                                validators=[DataRequired(
                                    'Please enter a name.')])
    new_user_pass = PasswordField('new_user_pass',
                                  validators=[DataRequired(
                                      'Please Enter a password.')])
    new_user_email = EmailField('new_user_email',
                                validators=[DataRequired(
                                    'Please enter a email.')])
    new_user_uid = StringField('new_user_uid',
                               validators=[DataRequired(
                                   'Please Enter your NetID')])
    new_user_major = StringField('new_user_major')
    new_user_grad = DateField('new_user_grad')
