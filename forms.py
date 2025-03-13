from wtforms import validators
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, IntegerField
from wtforms.form import Form
from wtforms.validators import DataRequired, Length
from psycopg2 import Timestamp
from wtforms import DateField


class TripForm(Form):
    departure = StringField('Departure', validators=[DataRequired(), Length(min=1, max=50)])
    destination = StringField('Destination', validators=[DataRequired(), Length(min=1, max=50)])
    departure_time = DateField('Departure Time', format='%y-%m-%d %H:%M', validators=[DataRequired(), Length(min=5, max=50)])

    available_seats = IntegerField('Available Seats', validators=[DataRequired(), Length(min=1, max=50)])
    created_at = Timestamp




class ContactForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')

# TODO: auth forms
class RegisterForm(Form):
    name = StringField('name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    role = StringField('Role', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Submit')

class BookingForm(Form):
    trip_id = IntegerField('Trip ID', validators=[DataRequired()])
    passenger_id = IntegerField('Passenger ID', validators=[DataRequired()])
