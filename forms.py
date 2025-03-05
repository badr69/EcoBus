from wtforms import validators
from wtforms.fields.simple import StringField, TextAreaField, SearchField, SubmitField, BooleanField, PasswordField
from wtforms.form import Form
from wtforms.validators import DataRequired


class ContactForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(Form):
    name = StringField('name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    submit = SubmitField('Submit')
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])

class LoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Submit')
