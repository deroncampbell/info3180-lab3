from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TextField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class ContactForm(FlaskForm):

    name = StringField("Please enter your full name",validators=[DataRequired()])
    email = StringField("Please enter your e-mail address", validators=[DataRequired()])
    subject = StringField("Please enter the subject for your message", validators=[DataRequired()])
    message = TextAreaField("Please enter the message you would like to send", validators=[DataRequired()])

    submit = SubmitField('Send')


