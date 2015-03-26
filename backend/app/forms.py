from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(Form):
    user_name = StringField('user_name', validators=[DataRequired()])
    user_pass = StringField('user_pass', validators=[DataRequired()])
