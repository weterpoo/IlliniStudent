from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    user_name = StringField('user_name', validators=[DataRequired()])
    user_pass = PasswordField('user_pass', validators=[DataRequired()])
